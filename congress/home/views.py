from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django import http

# Create your views here.
def home(request):
    user = request.user
    if user.is_authenticated:
        if user.is_superuser:
            return redirect('home:admin')
        else:
            return redirect('home:participant')
    return render(request, 'home/home.html')

@login_required
def admin(request):
    if request.user.is_superuser:
        return render(request, 'home/administrator.html')
    else:
        raise http.Http404

@login_required
def participant(request):
    if hasattr(request.user, 'participant'):
        return render(request, 'home/participant.html')
    else:
        raise http.Http404