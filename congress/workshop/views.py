from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy

from .models import Workshop
from .forms import WorkshopForm

class WorkshopListView(ListView):
    model = Workshop
    template_name = 'workshop/list.html'
    context_object_name = 'workshops'


class WorkshopDetailView(DetailView):
    model = Workshop
    template_name = 'workshop/detail.html'
    context_object_name = 'workshop'


class WorkshopCreateView(CreateView):
    model = Workshop
    form_class = WorkshopForm
    template_name = 'workshop/create.html'

    def get_success_url(self):
        return reverse_lazy('workshop:list')


class WorkshopUpdateView(UpdateView):
    model = Workshop
    template_name = 'workshop/update.html'
    fields = '__all__'