from django.shortcuts import render

# Create your views here.
from workouts.models import Workout
from nutrition.models import FoodEntry


from django.shortcuts import render
from datetime import date

def landing_view(request):
    return render(request, 'landing.html')

def dashboard_view(request):
    user = request.user
    today = date.today()

    recent_workouts = Workout.objects.filter(user=user).order_by('-created_at')[:5]
    recent_foods = FoodEntry.objects.filter(user=user).order_by('-created_at')[:5]
    today_foods = FoodEntry.objects.filter(user=user, date=today)

    # Nutrition summary
    total_calories = sum(food.calories for food in today_foods)
    total_protein = sum(food.protein_g for food in today_foods)
    total_fat = sum(food.fat_total_g for food in today_foods)
    total_carbs = sum(food.carbohydrates_total_g for food in today_foods)

    context = {
        'recent_workouts': recent_workouts,
        'recent_foods': recent_foods,
        'nutrition_summary': {
            'calories': round(total_calories, 2),
            'protein': round(total_protein, 2),
            'fat': round(total_fat, 2),
            'carbs': round(total_carbs, 2),
        }
    }
    
    return render(request, 'dashboard.html',context)