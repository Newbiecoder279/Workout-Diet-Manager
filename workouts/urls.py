from django.urls import path
from . import views

urlpatterns = [
    # Workout URLs
    path('workouts/new/', views.create_workout, name='workout_create'),
    path('workouts/<int:pk>/edit/', views.WorkoutUpdateView.as_view(), name='workout_edit'),
    path('workouts/', views.WorkoutListView.as_view(), name='workout_list'),
    path('workouts/<int:pk>/', views.WorkoutDetailView.as_view(), name='workout_detail'),
]