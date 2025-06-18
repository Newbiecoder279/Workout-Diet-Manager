from django import forms
from .models import Workout, WorkoutExercises
from django.forms import inlineformset_factory

class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['duration', 'notes']
        widgets = {
            'duration': forms.TimeInput(attrs={'type': 'time'}),
            'notes': forms.Textarea(attrs={'rows': 3}),
        }

WorkoutExerciseFormSet = inlineformset_factory(
    Workout,
    WorkoutExercises,
    fields = ['exercise_name', 'muscle_group', 'equipment_used', 'sets', 'reps', 'weight'],
    extra = 1,
    can_delete=True,
    widgets = {
        'exercise_name': forms.TextInput(attrs={'class': 'form-control'}),
        'muscle_group': forms.Select(attrs={'class': 'form-control'}),
        'equipment_used': forms.TextInput(attrs={'class': 'form-control'}),
        'sets': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
        'reps': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
        'weight': forms.NumberInput(attrs={'class': 'form-control', 'min': 0, 'step': '0.1'}),
    }
)
