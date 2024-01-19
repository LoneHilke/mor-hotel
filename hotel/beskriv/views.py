from django.shortcuts import render, redirect
from django.views import View
from info.models import Beskrivelse
# Create your views here.
class Beskriv(View):
  def get(self, request, *args, **kwargs):

    beskrivelse = Beskrivelse.objects.all()
    context = {

        'beskrivelse':beskrivelse,
      } 

    return render(request, 'beskriv/beskriv.html', context)