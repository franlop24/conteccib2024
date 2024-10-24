from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy

from .models import Participant
from .forms import ParticipantCreateForm

class ParticipantCreateView(CreateView):
    model = Participant
    form_class = ParticipantCreateForm
    template_name = 'participant/participant_register.html'
    success_url = reverse_lazy('login')

    