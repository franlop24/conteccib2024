from django import forms

from .models import Participant
from django.contrib.auth.forms import UserCreationForm

    
class ParticipantCreateForm(UserCreationForm):
    class Meta:
        model = Participant
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

class ParticipantUpdateForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ('first_name', 'last_name', 'lastname_mat', 'username', 'email', 'enrollment', 'career', 'semester', 'phone', 'photo')

class SearchParticipantForm(forms.Form):
    search = forms.CharField(max_length=100, required=True, label='Buscar')


class ValidateParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['folio']
