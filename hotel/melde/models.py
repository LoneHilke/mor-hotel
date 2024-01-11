from django.db import models

# Create your models here.
class Melde(models.Model):
    brugernavn = models.CharField(max_length=50)
    adgangskode = models.CharField(max_length=50)

    def __str__(self):
        return self.brugernavn