from django.urls import path
from .views import dashboard_view, landing_view

urlpatterns = [
    path('', landing_view, name='landing' ),
    path('dashboard/', dashboard_view, name='dashboard'),
]
