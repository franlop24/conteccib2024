from django.db import models
from django.contrib.auth.models import User

from workshop.models import Workshop

# class Professor(User):
#     lastname_mat = models.CharField(max_length=50, verbose_name="Apellido materno")
#     title = models.CharField(max_length=50, verbose_name="Título", default='Ing.')
    
#     def get_full_name(self):
#         return f"{ self.title } { self.first_name } { self.last_name } { self.lastname_mat }"

#     def __str__(self):
#         return self.get_full_name()
    

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
    career = models.CharField(max_length=100, verbose_name="Carrera", default='Ingeniería en Sistemas Computacionales')
    semester = models.IntegerField(verbose_name="Cuatrimestre", choices=SEMESTERS, default=1)
    #tutor = models.ForeignKey(Professor, on_delete=models.CASCADE, verbose_name="Tutor", related_name='tutor')
    workshop = models.ForeignKey(Workshop, on_delete=models.CASCADE, 
                                 verbose_name="Taller", related_name='workshop',
                                 blank=True, null=True)
    
    def get_full_name(self):
        return f"{ self.enrollment } { self.first_name } { self.last_name } { self.lastname_mat }"

    def __str__(self):
        return self.get_full_name()