from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Workshop
from .forms import WorkshopForm
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator

class WorkshopListView(ListView):
    model = Workshop
    template_name = 'workshop/list.html'
    context_object_name = 'workshops'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = [workshop for workshop in queryset if workshop.available_seats > 0]
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