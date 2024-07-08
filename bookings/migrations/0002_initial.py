# Generated by Django 5.0.6 on 2024-07-08 13:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bookings', '0001_initial'),
        ('hotels', '0001_initial'),
        ('room_services', '0001_initial'),
        ('rooms', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='guests',
            field=models.ManyToManyField(to='user.guest'),
        ),
        migrations.AddField(
            model_name='booking',
            name='hotel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='hotel_bookings', to='hotels.hotel'),
        ),
        migrations.AddField(
            model_name='booking',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='rooms', to='rooms.room'),
        ),
        migrations.AddField(
            model_name='booking',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='booking_services', to='room_services.roomservice'),
        ),
    ]
