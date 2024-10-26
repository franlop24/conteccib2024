from django.db import models
from django.contrib.auth.models import User

from workshop.models import Workshop

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
    lastname_mat = models.CharField(max_length=50, verbose_name="Apellido materno")
    enrollment = models.CharField(max_length=10, verbose_name="Matrícula")
    folio = models.CharField(max_length=10, verbose_name="Folio", default='0000')
    is_valid = models.BooleanField(default=False)
    career = models.CharField(max_length=100, verbose_name="Carrera", default='IDGS')
    semester = models.CharField(max_length=15, verbose_name="Cuatrimestre", choices=SEMESTERS, default='Primero')
    phone = models.CharField(max_length=10, verbose_name="Teléfono", default='0000000000')
    workshop = models.ForeignKey(Workshop, on_delete=models.CASCADE, 
                                 verbose_name="Taller", related_name='workshop',
                                 blank=True, null=True)
    photo = models.ImageField(upload_to=custom_upload_to, verbose_name="Foto", blank=True, null=True)
    
    def get_full_name(self):
        return f"{ self.first_name } { self.last_name } { self.lastname_mat }"

    def __str__(self):
        return f"{ self.enrollment } {self.get_full_name()}"