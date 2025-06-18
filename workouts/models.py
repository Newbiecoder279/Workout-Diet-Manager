from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Workout(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   duration = models.DurationField(help_text="Duration of you workout")
   notes = models.TextField(blank=True, help_text="Any additional notes")
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now_add=True)
   
   def __str__(self):
       return f"Workout on {self.created_at.strftime('%Y-%m-%d')}"


class WorkoutExercises(models.Model):
    MUSCLE_GROUPS = [
        ('chest','Chest'),
        ('back','Back'),
        ('legs','Legs'),
        ('shoulders','Shoulders'),
        ('arms','Arms'),
        ('core','Core'),
        ('full_body','Full Body')
    ]
    
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE, related_name='exercises')
    exercise_name = models.CharField(max_length=100)
    muscle_group = models.CharField(max_length=20, choices=MUSCLE_GROUPS)
    equipment_used = models.CharField(max_length=100, blank = True)
    sets = models.PositiveIntegerField()
    reps = models.PositiveIntegerField()
    weight = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, help_text="Weight in kg/lbs")
    
    
    def __str__(self):
        return f"{self.exercise_name} ({self.sets}x{self.reps})"
    
    