from django import forms
from .models import User, Car


class Logingform(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
