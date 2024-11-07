from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import CreateView, ListView, UpdateView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from .models import Participant
from .forms import (ParticipantCreateForm, SearchParticipantForm, 
                    ValidateParticipantForm, ParticipantUpdateForm)

class ParticipantCreateView(CreateView):
    model = Participant
    form_class = ParticipantCreateForm
    template_name = 'participant/participant_register.html'
    success_url = reverse_lazy('login')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home:home')
        return super().dispatch(request, *args, **kwargs)

class ParticipantListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    def test_func(self):
        return self.request.user.is_staff
    model = Participant
    template_name = 'participant/participant_list.html'
    context_object_name = 'participants'
    paginate_by = 20

    def get_queryset(self):
        search = self.request.GET.get('search', '')
        tutor = self.request.GET.get('tutor', '')
        if search:
            return Participant.objects.filter(first_name__icontains=search).order_by('last_name')
        if tutor:
            return Participant.objects.filter(tutore=tutor).order_by('last_name')
        return Participant.objects.all().order_by('last_name')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = SearchParticipantForm()
        return context


class ParticipantUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    def test_func(self):
        return self.request.user.is_staff or self.request.user.participant.pk == self.kwargs['pk']
    model = Participant
    form_class = ParticipantUpdateForm
    template_name = 'participant/participant_update.html'

    def get_success_url(self):
        return reverse_lazy('participant:detail', kwargs={'pk': self.object.pk})

    def get_object(self):
        return get_object_or_404(Participant, pk=self.kwargs['pk'])
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['participant'] = self.get_object()
        return context


class ParticipantDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    def test_func(self):
        return self.request.user.is_staff or self.request.user.participant.pk == self.kwargs['pk']
    model = Participant
    template_name = 'participant/participant_detail.html'
    context_object_name = 'participant'


@staff_member_required(login_url='login')
@login_required
def validate_participant(request, pk):
    participant = get_object_or_404(Participant, pk=pk)
    form = ValidateParticipantForm(instance=participant)
    if request.method == 'POST':
        form = ValidateParticipantForm(request.POST, instance=participant)
        if form.is_valid():
            participant.is_valid = True
            participant.save()
            return redirect('participant:list')
    return render(request, 'participant/participant_validate.html', {'form': form, 'participant': participant})