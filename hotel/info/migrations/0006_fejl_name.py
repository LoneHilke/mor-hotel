# Generated by Django 4.1.5 on 2024-01-20 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0005_fejl_beskrivelse_nr_dinner_nr_reservation_nr'),
    ]

    operations = [
        migrations.AddField(
            model_name='fejl',
            name='name',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
