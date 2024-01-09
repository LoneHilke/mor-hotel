from django.contrib import admin
from .models import Beskrivelse, Reservation, Dinner

# Register your models here.
admin.site.register(Beskrivelse)
admin.site.register(Reservation)
admin.site.register(Dinner)
