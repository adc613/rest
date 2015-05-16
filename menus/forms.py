from django import forms

from .models import Menu, MenuItem

class MenuCreationForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ['title']

class MenuItemCreationForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ['description', 'price', 'title']
