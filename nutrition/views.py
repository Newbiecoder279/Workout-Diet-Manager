import requests
from django.shortcuts import render
from .forms import FoodEntryForm, GetInfoForm
from django.contrib.auth.decorators import login_required
from . models import FoodEntry
@login_required
def addfood(request):
    nutrition_data = []

    if request.method == 'POST':
        form = FoodEntryForm(request.POST)
        if form.is_valid():
            food = form.save(commit=False)
            food.user = request.user

            food_name = form.cleaned_data['food']
            food_weight = form.cleaned_data['quantity']
            query = f"{food_weight}g {food_name}"

            api_url = 'https://api.calorieninjas.com/v1/nutrition?query='
            response = requests.get(api_url + query, headers={'X-Api-Key': 'Z/LpACaI7e6ohZKXhijixA==g7fppn0yyTx22Gxs'})

            if response.status_code == requests.codes.ok:
                nutrition_data = response.json()
                print(response.text)

                items = nutrition_data.get('items', [])
                if items:
                    item = items[0]
                    food.calories = item.get('calories',0)
                    food.protein_g = item.get('protein_g',0)
                    food.fat_total_g= item.get('fat_total_g', 0)
                    food.carbohydrates_total_g = item.get('carbohydrates_total_g',0)
                else:
                    print("⚠️ No nutrition items found for query:", query)
            else:
                print("Error:", response.status_code, response.text)

            food.save()  # ✅ Save after everything is added
    else:
        form = FoodEntryForm()

    return render(request, 'add_food.html', {'form': form, 'nutrition_data': nutrition_data})


def food_list_view(request):
    user = request.user
    foods = FoodEntry.objects.filter(user=user)
    
    return render(request, 'food_list.html', {'foods':foods})

def get_info_view(request):
    if request.method == "POST":
        get_info_form = GetInfoForm(request.POST)
        
        if get_info_form.is_valid():
            data = get_info_form.save(commit=False)
            data.user = request.user
            get_info_form.save()
            
    else:
         get_info_form = GetInfoForm()
    
    return render(request, 'get_info.html', {'get_info_form':get_info_form})