# Generated by Django 4.1.5 on 2024-01-21 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0007_reservation_rejse'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='kontakt',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
