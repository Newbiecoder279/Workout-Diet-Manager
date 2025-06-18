from django.shortcuts import render, redirect
from . forms import CreateUserForm
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
            
    else:
        
        form = CreateUserForm()
            
    return render(request, 'signup.html',{'form':form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data = request.POST)
        
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
        
    return render(request, 'login.html', {'form':form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('landing')
    
@login_required
def dashboard(request):
    return render (request,'dashboard/dashboard.html')
