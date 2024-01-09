from django.db import models

# Create your models here.
class Beskrivelse(models.Model):
    str = models.TextField()
    belig = models.TextField()
    antal = models.IntegerField()
    beskriv = models.TextField()
    opred = models.BooleanField(default=True)

    def __str__(self):
        return self.str

class Reservation(models.Model):
    name = models.TextField()
    dato = models.DateField(blank=True, null=True)
    person = models.IntegerField()
    pris = models.CharField(max_length = 250)

    def __str__(self):
        return self.name

class Dinner(models.Model):
    morgen = models.TextField()
    middag = models.TextField()
    aften = models.TextField()

    def __str__(self):
        return self.morgen

