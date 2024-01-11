from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Melde
from .forms import MeldeForm
from django.views import View
from django.urls import reverse
from django.views.generic import TemplateView, ListView
from django.template import loader

def index(request):
  return render(request, 'meld/base.html', {'title':'index'})

def melde(request):
  melder = Melde.objects.all()
  form = MeldeForm()

  if request.method == 'POST':
    form = MeldeForm(request.POST)
    if form.is_valid():
        form.save()
    return redirect('/')

  context = {'melder': melder, 'form': form}
  return render(request, 'meld/login.html', context)

def update(request, pk):
  melde = Melde.objects.get(id=pk)
  form = MeldeForm(instance=melde) 
  context = {'form': form}
  if request.method == 'POST':
    form = MeldeForm(request.POST, instance=melde) 
    if form.is_valid():
        form.save()
        return redirect('/')
  
  return render(request, 'meld/update.html', context)

def komind(request):
  if request.method == 'POST':
    # Hent input fra skjemaet
    input_data = request.POST.get('brugernavn')
    input_data1 = request.POST.get('adgangskode')

    # Gjør sammenligning med modellen (dette er et eksempel, tilpass etter behov)
    if Melde.objects.filter(brugernavn=input_data).exists():
      if Melde.objects.filter(adgangskode=input_data1).exists():
        # Rediriger til en annen side hvis sammenligningen er vellykket
        return redirect('/personale')  # Erstatt 'annen_side_navn' med faktisk navn på den andre siden
    else:
        # Hvis sammenligningen mislykkes, gjør noe annet (f.eks. vis feilmelding)
        return render(request, 'meld/login.html', {'feilmelding': 'Ugyldig input!'})

  # Hvis ikke en POST-request, render visningens template
  return render(request, 'meld/komind.html')