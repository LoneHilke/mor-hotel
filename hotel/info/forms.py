from django import forms
from django.forms import ModelForm
from .models import Reservation, Dinner, Fejl

"""class TaskForm(forms.ModelForm):
  name = forms.CharField(
    widget= forms.TextInput(
    attrs={'placeholder': 'Add new task...'}))

  class Meta:
      model = Task
      fields = '__all__'"""
    
class ReservationForm(forms.ModelForm):
  name = forms.CharField(
    widget = forms.TextInput(
      attrs={'placeholder': 'Ny reservation...'}
    ))

  class Meta:
      model = Reservation
      fields = '__all__'

class DinnersForm(forms.ModelForm):
  name = forms.CharField(
    widget = forms.TextInput(
      attrs={'placeholder': 'Dinner'}
    ))

  class Meta:
      model = Dinner
      fields = '__all__'

class FejlForm(forms.ModelForm):
  name = forms.CharField(
    widget = forms.TextInput(
      attrs={'placeholder': 'Fejl'}
    ))

  class Meta:
      model = Fejl
      fields = '__all__'