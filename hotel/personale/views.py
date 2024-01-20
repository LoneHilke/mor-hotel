from django.shortcuts import render, redirect
from django.views import View
from info.models import Reservation, Dinner, Fejl

# Create your views here.
class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'personale/base.html')
    
class Personale(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'personale/personale.html')
    
def middag(request):
    #def get(self, request, *args, **kwargs):
         
      dinner = Dinner.objects.all()
      context = {

        'dinner':dinner,
      }
     
      return render(request, 'personale/dinner.html', context)

def reservation(request):
    #def get(self, request, *args, **kwargs):
         
      reservation = Reservation.objects.all()
      context = {

        'reservation':reservation,
      }
     
      return render(request, 'personale/reservation.html', context)

def mangler(request):
    #def get(self, request, *args, **kwargs):
         
      fejl = Fejl.objects.all()
      context = {

        'fejl':fejl,
      }
     
      return render(request, 'personale/fejl.html', context)
