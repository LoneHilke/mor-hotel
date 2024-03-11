from django.shortcuts import render, redirect
from django.views import View
from .models import Beskrivelse, Oplev, Reservation, Dinner, Fejl
from .forms import ReservationForm, DinnersForm, FejlForm
from datetime import datetime

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

    return render(request, 'info/beskriv.html', context)
  
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
      return redirect('/afregn')
      
    context = {'reservation': reservation, 'form': form}
    return render(request, 'info/reserver.html', context)

"""def update_reserver(request, pk):
    reservation = Reservation.objects.get(id=pk)
    form = ReservationForm(instance=reservation) 
    context = {'form': form}
    if request.method == 'POST':
      form = ReservationForm(request.POST, instance=reservation) 
      if form.is_valid():
          form.save()
          return redirect('/')
    return render(request, 'info/update-reserver.html', context)"""

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

def dinner(request):
    dinner = Dinner.objects.all()
    form = DinnersForm()
  
    if request.method == 'POST':
      form = DinnersForm(request.POST)
      if form.is_valid():
        form.save()
      return redirect('/')
      
    context = {'dinner': dinner, 'form': form}
    return render(request, 'info/menu.html', context)

def fejl(request):
    fejl = Fejl.objects.all()
    form = FejlForm()
  
    if request.method == 'POST':
      form = FejlForm(request.POST)
      if form.is_valid():
        form.save()
      return redirect('/')
      
    context = {'fejl': fejl, 'form': form}
    return render(request, 'info/fejl.html', context)

"""class Afregn(View):
    def get(self, request, *args, **kwargs):
         
          reservation = Reservation.objects.all()
          context = {

            'reservation':reservation,
          }
     
          return render(request, 'info/afregn.html', context)
    
    def post(self, request, *args, **kwargs):
       kontakt = request.POST.get('kontakt')
       order_afregn = {
          'reservation' : []
       }

       reservation = request.POST.getlist('reservation[]')

       for reserv in reservation:
          reservation = Reservation.objects.get(pk__contains=reserv(reservation))
          reserv_data={
             'id': reservation.pk,
             'kontakt': reservation.kontakt,
             'pris': reservation.pris
          }

          order_afregn['reservation'].append(reserv_data)

          pris = 0
          reserv_ids = []

       for afregn in order_afregn['reservation']:
          pris += reserv['pris']
          reserv_ids.append(reserv['id'])

          return redirect('reserv-confirmations', pk=reserv.pk)"""

class Afregn(View):
   def get(self, request):
      
      reservation = Reservation.objects.all()
      form = ReservationForm()
      date_format = "%d/%m/%Y"
      dato = datetime.strptime('10/04/2024', date_format)
      rejse = datetime.strptime('12/04/2024', date_format)

      delta = rejse - dato
      date_diff = delta.days
      context = {

            'reservation':reservation,
            'form':form,
            'date_diff': date_diff,
      }
      return render(request, 'info/afregn.html', context)

