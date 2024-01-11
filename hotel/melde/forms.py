from django import forms
from django.forms import ModelForm
from .models import Melde

class MeldeForm(forms.ModelForm):
  name = forms.CharField(
    widget= forms.TextInput(
    attrs={'placeholder': 'Add new login...'}))

  class Meta:
      model = Melde
      fields = '__all__'