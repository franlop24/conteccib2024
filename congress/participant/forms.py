from django import forms
from django.contrib.auth.forms import UserCreationForm

from tutor.models import Tutor

from .models import Participant
from .validators import validate_image

    
class ParticipantCreateForm(UserCreationForm):
    class Meta:
        model = Participant
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')


class ParticipantUpdateForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ('first_name', 'last_name', 'lastname_mat', 'username', 'email', 'tutore', 'career', 'enrollment', 'semester', 'phone', 'photo')
        widgets = {
            'photo': forms.FileInput(attrs={'required': False})
        }

    def clean_photo(self):
        photo = self.cleaned_data.get('photo')
        validate_image(photo)  # Llama a la validación personalizada
        return photo


class SearchParticipantForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label='Buscar')
    tutor = forms.ModelChoiceField(queryset=Tutor.objects.all(), required=False, label='Tutor')


class ValidateParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['folio']
