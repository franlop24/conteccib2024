from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tutor(User):
    lastname_mat = models.CharField(max_length=50, verbose_name="Apellido Materno", default='', blank=True, null=True)

    @property
    def full_name(self):
        if self.lastname_mat:
            return f"{ self.first_name } { self.last_name } { self.lastname_mat }"
        else:
            return f"{ self.first_name } { self.last_name }"

    def __str__(self):
        return self.full_name