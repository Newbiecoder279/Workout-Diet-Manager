from django.urls import path
from . import views


urlpatterns = [
    path('entry/',views.addfood, name='addfood'),
    path('list/',views.food_list_view, name='foodlist'),
    path('get_info/', views.get_info_view, name='getinfo' )
    
]
