from django import forms
from . models import FoodEntry, GetInfo

class FoodEntryForm(forms.ModelForm):
    class Meta:
        model = FoodEntry
        fields = ['food','quantity']
        
class GetInfoForm(forms.ModelForm):
    class Meta:
        model = GetInfo
        exclude = ['user']