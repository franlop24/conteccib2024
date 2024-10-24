from django import forms

from .models import Participant
from django.contrib.auth.forms import UserCreationForm

    
class ParticipantCreateForm(UserCreationForm):
    class Meta:
        model = Participant
        fields = ('username', 'email', 'password1', 'password2')