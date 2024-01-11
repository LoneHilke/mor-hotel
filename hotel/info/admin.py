from django.contrib import admin
from .models import Beskrivelse, Reservation, Dinner, Oplev

# Register your models here.
admin.site.register(Beskrivelse)
admin.site.register(Reservation)
admin.site.register(Dinner)
admin.site.register(Oplev)