from django import forms

from tutor.models import Tutor

class TutorCreateForm(forms.ModelForm):
    class Meta:
        model = Tutor
        fields = ['first_name', 'last_name', 'lastname_mat', 'email']    
        labels = {
            'last_name': 'Apellido Paterno',
            'lastname_mat': 'Apellido Materno'
        }
        widgets = {
            'email': forms.EmailInput(attrs={'required': True})
        }
        # help_texts = {
        #     'email': 'el usuario y contraseña se generan apartir del correo ejem peter@mail.com Usuario: peter, password: peter'
        # }