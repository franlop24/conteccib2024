from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from .forms import TutorCreateForm
from .models import Tutor

class TutorListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    def test_func(self):
        return self.request.user.is_staff
    model = Tutor
    template_name = 'tutor/tutor_list.html'
    context_object_name = 'tutors'

@login_required
@staff_member_required(login_url='login')
def create_tutor(request):
    if request.method == 'POST':
        form = TutorCreateForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            
            username = email
            password = email.split('@')[0]

            p = Tutor.objects.create_user(email = email, username = username, password = password)
            p.first_name = form.cleaned_data['first_name']
            p.last_name = form.cleaned_data['last_name']
            p.lastname_mat = form.cleaned_data['lastname_mat']
            p.is_staff = True
            p.is_superuser = True
            p.save()

            return redirect('tutor:list')
    else:
        form = TutorCreateForm()
    return render(request, 'tutor/tutor_create.html', {'form': form})