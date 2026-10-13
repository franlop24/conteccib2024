from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import transaction
from django.views.decorators.http import require_POST

from .models import Workshop, Instructor
from .forms import WorkshopForm, InstructorCreateForm
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator

class WorkshopListView(ListView):
    model = Workshop
    template_name = 'workshop/list.html'
    context_object_name = 'workshops'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset

class WorkshopDetailView(DetailView):
    model = Workshop
    template_name = 'workshop/detail.html'
    context_object_name = 'workshop'

class WorkshopCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    def test_func(self):
        return self.request.user.is_staff
    model = Workshop
    form_class = WorkshopForm
    template_name = 'workshop/create.html'

    def get_success_url(self):
        return reverse_lazy('workshop:list')

class WorkshopUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    def test_func(self):
        return self.request.user.is_staff
    model = Workshop
    form_class = WorkshopForm
    template_name = 'workshop/update.html'
    success_url = reverse_lazy('workshop:list')

@login_required
@require_POST
def workshop_register(request, pk):
    participant = getattr(request.user, 'participant', None)
    if participant is None:
        messages.error(request, 'Esta cuenta no tiene un perfil de participante.')
        return redirect('workshop:detail', pk=pk)

    with transaction.atomic():
        # Lock the participant first so simultaneous requests cannot enroll the
        # same account in two different workshops.
        participant = participant.__class__.objects.select_for_update().get(pk=participant.pk)
        workshop = get_object_or_404(Workshop.objects.select_for_update(), pk=pk)

        if not participant.is_valid:
            messages.error(request, 'Tu folio debe validarse antes de inscribirte.')
        elif participant.workshop_id == workshop.pk:
            messages.info(request, 'Ya estás inscrito en este taller.')
        elif participant.workshop_id:
            messages.error(request, 'Ya estás inscrito en otro taller.')
        elif workshop.seats_occuped >= workshop.seats:
            messages.error(request, 'Lo sentimos, ya se llenó el taller. Elige otro, por favor.')
        else:
            participant.workshop = workshop
            participant.save(update_fields=['workshop'])
            # Retain the legacy counter as a cache, synchronized from the
            # authoritative participant relation while the workshop is locked.
            workshop.seats_occupied = workshop.seats_occuped
            workshop.save(update_fields=['seats_occupied'])
            messages.success(request, 'Te inscribiste correctamente al taller.')

    return redirect('workshop:detail', pk=pk)

class InstructorListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    def test_func(self):
        return self.request.user.is_staff
    model = Instructor
    template_name = 'workshop/instructor_list.html'
    context_object_name = 'instructors'

class InstructorUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    def test_func(self):
        return self.request.user.is_staff
    model = Instructor
    form_class = InstructorCreateForm
    template_name = 'workshop/instructor_update.html'
    context_object_name = 'instructor'
    success_url = reverse_lazy('workshop:instructor_list')

@login_required
@staff_member_required(login_url='login')
def create_instructor(request):
    if request.method == 'POST':
        form = InstructorCreateForm(request.POST, request.FILES)
        if form.is_valid():
            email = form.cleaned_data['email']
            username = email
            password = email.split('@')[0]

            instructor = Instructor.objects.create_user(email=email, username=username, password=password)
            instructor.first_name = form.cleaned_data['first_name']
            instructor.last_name = form.cleaned_data['last_name']
            instructor.title = form.cleaned_data['title']
            instructor.photo = form.cleaned_data['photo']
            instructor.semblanza = form.cleaned_data['semblanza']
            instructor.is_staff = True
            instructor.save()

            return redirect('workshop:instructor_list')
    else:
        form = InstructorCreateForm()
    return render(request, 'workshop/instructor_create.html', {'form': form})
