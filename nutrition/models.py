from django.db import models
from django.contrib.auth.models import User


    
class FoodEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    food = models.CharField(max_length=25)
    quantity = models.PositiveIntegerField(help_text="Quantity in grams")
    calories = models.FloatField(null=True, blank = True)
    protein_g = models.FloatField(null=True, blank = True)
    fat_total_g = models.FloatField(null=True, blank = True)
    carbohydrates_total_g = models.FloatField(null=True, blank = True)
    date = models.DateField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.food
    
class GetInfo(models.Model):
    
    GENDER_CHOICES = [
        ('male','Male'),
        ('female','Female')
    ]
    ACTIVITY_LEVEL_CHOICES = [
        ('sednetary','Sedentary'),
        ('light','Light'),
        ('moderate','Moderate'),
        ('active','Active'),
        ('very_active','Very Active')
    ]
    GOALS = [
        ('lose','Lose'),
        ('maintain','Maintain'),
        ('gain','Gain')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    height_cm = models.PositiveIntegerField()
    weight_kg = models.PositiveIntegerField()
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10,choices=GENDER_CHOICES)
    activity_level = models.CharField(max_length=20,choices=ACTIVITY_LEVEL_CHOICES)
    goal = models.CharField(max_length=15,choices=GOALS)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username}'s info"