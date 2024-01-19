from django.db import models

# Create your models here.
class Beskrivelse(models.Model):
    nr = models.IntegerField(blank=True)
    str = models.TextField()
    belig = models.TextField()
    antal = models.IntegerField()
    beskriv = models.TextField()
    pris = models.FloatField()
    opred = models.BooleanField(default=True)

    def __str__(self):
        return self.str

class Reservation(models.Model):
    nr = models.IntegerField(blank=True)
    name = models.TextField()
    dato = models.DateField(blank=True, null=True)
    person = models.IntegerField()
    pris = models.CharField(max_length = 250)

    def __str__(self):
        return self.name

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

    def __str__(self):
        return self.nr