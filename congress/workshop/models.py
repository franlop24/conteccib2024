from django.db import models
from django.utils import timezone

# Create your models here.
class Workshop(models.Model):
    title = models.CharField(max_length=150, verbose_name='Título')
    description = models.TextField(verbose_name='Descripción', blank=True, null=True, default=None)
    name_ponent = models.CharField(max_length=150, verbose_name='Nombre del ponente', blank=True, null=True, default=None)
    title_ponent = models.CharField(max_length=150, verbose_name='Título del ponente', blank=True, null=True, default=None)
    place = models.CharField(max_length=150, verbose_name='Lugar', blank=True, null=True, default=None)
    date = models.DateField(verbose_name='Día', blank=True, null=True, default=timezone.now)
    initial_hour = models.TimeField(verbose_name='Hora de inicio', blank=True, null=True, default=None)
    final_hour = models.TimeField(verbose_name='Hora de fin', blank=True, null=True, default=None)
    seats = models.IntegerField(verbose_name='Lugares disponibles', default=0)
    seats_occupied = models.IntegerField(verbose_name='Lugares ocupados', default=0)

    @property
    def is_full(self):
        return self.seats == self.seats_occupied
    
    @property
    def available_seats(self):
        return self.seats - self.seats_occupied
    
    def __str__(self):
        return self.title