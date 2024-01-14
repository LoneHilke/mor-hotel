from django.shortcuts import render, redirect
from django.views import View
from info.models import Reservation

# Create your views here.
class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'personale/base.html')
    
class Reservation(View):
    def get(self, request, *args, **kwargs):
         
      reservation = Reservation.objects.all()
      context = {

        'reservation':reservation,
      }
     
      return render(request, 'personale/reservation.html', context)