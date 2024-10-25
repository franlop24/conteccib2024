from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    user = request.user
    if user.is_authenticated:
        if user.is_superuser:
            return redirect('home:admin')
        else:
            return redirect('home:participant')
    return render(request, 'home/home.html')

def admin(request):
    return render(request, 'home/administrator.html')

def participant(request):
    return render(request, 'home/participant.html')