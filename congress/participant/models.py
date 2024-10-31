from django.db import models
from django.contrib.auth.models import User

from workshop.models import Workshop
from tutor.models import Tutor

def custom_upload_to(instance, filename):
    if instance.pk:
        old_instance = Participant.objects.get(pk=instance.pk)
        old_instance.photo.delete()
    return f'participants/{instance.pk}/{filename}'

class Participant(User):
    SEMESTERS = [
        ('Primero', 'Primero'),
        ('Segundo', 'Segundo'),
        ('Tercero', 'Tercero'),
        ('Cuarto', 'Cuarto'),
        ('Quinto', 'Quinto'),
        ('Sexto', 'Sexto'),
        ('Séptimo', 'Séptimo'),
        ('Octavo', 'Octavo'),
        ('Noveno', 'Noveno'),
        ('Décimo', 'Décimo'),
    ]
    lastname_mat = models.CharField(max_length=50, verbose_name="Apellido materno", null=True, blank=True)
    enrollment = models.CharField(max_length=10, verbose_name="Matrícula", null=True, blank=True, default='-')
    folio = models.CharField(max_length=10, verbose_name="Folio", unique=True, null=True, blank=True)
    is_valid = models.BooleanField(default=False)
    career = models.CharField(max_length=100, verbose_name="Carrera", default='IDGS')
    semester = models.CharField(max_length=15, verbose_name="Cuatrimestre", choices=SEMESTERS, default='Primero')
    phone = models.CharField(max_length=10, verbose_name="Teléfono", default='0000000000')
    workshop = models.ForeignKey(Workshop, on_delete=models.SET_NULL,
                                 verbose_name="Taller", related_name='participants',
                                 blank=True, null=True)
    photo = models.ImageField(upload_to=custom_upload_to, verbose_name="Foto", blank=True, null=True)
    tutore = models.ForeignKey(Tutor, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Tutor')
    
    def get_full_name(self):
        if self.lastname_mat:
            return f"{ self.first_name } { self.last_name } { self.lastname_mat }"
        else:
            return f"{ self.first_name } { self.last_name }"
    def __str__(self):
        return self.get_full_name()