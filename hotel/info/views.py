from django.shortcuts import render, redirect
from django.views import View
#from .models import Plade, Runde, Category, Kant

# Create your views here.
class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'info/base.html')
    
class Info(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'info/info.html')
    
class Beskriv(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'info/Beskriv.html')