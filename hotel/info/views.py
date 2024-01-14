from django.shortcuts import render, redirect
from django.views import View
from .models import Beskrivelse, Oplev, Reservation, Dinner
from .forms import ReservationForm, DinnerForm


# Create your views here.
class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'info/forside.html')
    
class Info(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'info/info.html')
    
class Beskriv(View):
  def get(self, request, *args, **kwargs):

    beskrivelse = Beskrivelse.objects.all()
    context = {

        'beskrivelse':beskrivelse,
      } 

    return render(request, 'info/Beskriv.html', context)
  
class Opleve(View):
    def get(self, request, *args, **kwargs):
         
          oplev = Oplev.objects.all()
          context = {

            'oplev':oplev,
          }
     
          return render(request, 'info/oplev.html', context)
    

def Reserver(request):
    reservation = Reservation.objects.all()
    form = ReservationForm()
  
    if request.method == 'POST':
      form = ReservationForm(request.POST)
      if form.is_valid():
        form.save()
      return redirect('/')
      
    context = {'reservation': reservation, 'form': form}
    return render(request, 'info/reserver.html', context)

def update_reservation(request, pk):
    reservation = Reservation.objects.get(id=pk)
    form = ReservationForm(instance=reservation) 
    context = {'form': form}
    if request.method == 'POST':
      form = ReservationForm(request.POST, instance=reservation) 
      if form.is_valid():
          form.save()
          return redirect('/')
    return render(request, 'info/update-reservation.html', context)

class Kontakt(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'info/kontakt.html')
    
"""class Menu(View):
    def get(self, request, *args, **kwargs):
      dinner = Dinner.objects.all()
      form = DinnerForm()
    
      if request.method == 'POST':
        form = DinnerForm(request.POST)
        if form.is_valid():
          form.save()
        return redirect('/')
        
      context = {'dinner': dinner, 'form': form}
      return render(request, 'info/menu.html', context)"""

def Dinner(request):
    dinner = Dinner.objects.all()
    form = DinnerForm()
  
    if request.method == 'POST':
      form = DinnerForm(request.POST)
      if form.is_valid():
        form.save()
      return redirect('/')
      
    context = {'dinner': dinner, 'form': form}
    return render(request, 'info/menu.html', context)