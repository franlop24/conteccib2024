from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class Instructor(User):
    title = models.CharField(max_length=150, verbose_name='Título académico', blank=True, null=True)
    photo = CloudinaryField(
        verbose_name='Foto',
        blank=True,
        null=True,
        folder='instructores',
    )
    semblanza = models.TextField(verbose_name='Semblanza', blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Workshop(models.Model):
    title = models.CharField(max_length=150, verbose_name='Título')
    description = models.TextField(verbose_name='Descripción', blank=True, null=True, default=None)
    instructor = models.ForeignKey(Instructor, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Instructor", related_name="workshops")
    place = models.CharField(max_length=150, verbose_name='Lugar', blank=True, null=True, default=None)
    date = models.DateField(verbose_name='Día', blank=True, null=True, default=timezone.now)
    initial_hour = models.TimeField(verbose_name='Hora de inicio', blank=True, null=True, default=None)
    final_hour = models.TimeField(verbose_name='Hora de fin', blank=True, null=True, default=None)
    seats = models.IntegerField(verbose_name='Lugares disponibles', default=0)
    seats_occupied = models.IntegerField(verbose_name='Lugares ocupados', default=0)

    @property
    def is_full(self):
        return self.seats_occuped >= self.seats
    
    @property
    def seats_occuped(self):
        return self.participants.count()
    
    @property
    def available_seats(self):
        return max(0, self.seats - self.seats_occuped)
    
    def __str__(self):
        return self.title
