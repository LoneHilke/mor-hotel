from django.db import models
from datetime import datetime

# Create your models here.
class Beskrivelse(models.Model):
    nr = models.IntegerField(blank=True)
    str = models.TextField()
    belig = models.TextField()
    antal = models.IntegerField()
    beskriv = models.TextField()
    pris = models.FloatField()
    opred = models.BooleanField(default=True)
    telt = models.TextField(blank=True)

    def __str__(self):
        return self.str

class Reservation(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    nr = models.IntegerField(blank=True)
    telt = models.TextField(blank=True)
    name = models.TextField()
    dato = models.DateField(blank=True, null=True)
    rejse = models.DateField(blank=True, null=True)
    
    person = models.IntegerField()
    pris = models.IntegerField()
    kontakt = models.TextField(blank=True)

    def beregn_pris(self):
        # Beregn antal dage mellem startdato og slutdato
        antal_dage = (self.rejse - self.dato).days

        # Beregn den endelige pris ved at multiplicere antal dage med pris
        endelig_pris = antal_dage * self.pris

        return endelig_pris

    """def __str__(self):
        return self.name"""

class Dinner(models.Model):
    name = models.CharField(max_length=50, blank=True)
    nr = models.IntegerField(blank=True)
    morgen = models.TextField()
    middag = models.TextField()
    aften = models.TextField()

    def __str__(self):
        return self.morgen

class Oplev(models.Model):
    afstand = models.TextField()
    beskriv = models.TextField()
    foto = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.afstand
    
class Fejl(models.Model):
    nr = models.IntegerField(blank=True)
    fejl = models.TextField()
    mangler = models.TextField()
    forslag = models.TextField()
    name = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.nr