from django.shortcuts import render, redirect
from django.views import View
from .models import Beskrivelse, Reservation, Dinner, Oplev

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
  
class Oplev(View):
    def get(self, request, *args, **kwargs):
         
         oplev = Oplev.objects.all()
         context = {

           'oplev':oplev,
         }
     
         return render(request, 'info/oplev.html', context)