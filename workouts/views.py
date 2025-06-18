# views.py
from django.shortcuts import render, redirect
from .forms import WorkoutForm, WorkoutExerciseFormSet
from . models import Workout, WorkoutExercises
from django.views.generic import CreateView, UpdateView
from django.views.generic import ListView, DetailView

def create_workout(request):
    if request.method == 'POST':
        workout_form = WorkoutForm(request.POST)
        formset = WorkoutExerciseFormSet(request.POST)

        if workout_form.is_valid() and formset.is_valid():
            workout = workout_form.save(commit=False)
            workout.user = request.user
            workout.save()

            for form in formset:
                if form.cleaned_data and not form.cleaned_data.get('DELETE', False):
                    WorkoutExercises.objects.create(
                        workout=workout,
                        exercise_name=form.cleaned_data['exercise_name'],
                        muscle_group=form.cleaned_data['muscle_group'],
                        equipment_used=form.cleaned_data['equipment_used'],
                        sets=form.cleaned_data['sets'],
                        reps=form.cleaned_data['reps'],
                        weight=form.cleaned_data['weight']
                    )

            return redirect('workout_list')  # Or your success page

    else:
        workout_form = WorkoutForm()
        formset = WorkoutExerciseFormSet()

    return render(request, 'workout_form.html', {
        'form': workout_form,
        'formset': formset,
    })

    
class WorkoutUpdateView(UpdateView):
    model = Workout
    form_class = WorkoutForm
    template_name = 'workout_form.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = WorkoutExerciseFormSet(self.request.POST, instance=self.object)
        else:
            context['formset'] = WorkoutExerciseFormSet(instance=self.object)
        return context
    
    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        if formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return redirect('workout_detail', pk=self.object.pk)  # Redirect to workout detail
        else:
            return self.render_to_response(self.get_context_data(form=form))
        
        


class WorkoutListView(ListView):
    model = Workout
    template_name = 'workout_list.html'
    context_object_name = 'workouts'
    ordering = ['-created_at']

class WorkoutDetailView(DetailView):
    model = Workout
    template_name = 'workout_detail.html'