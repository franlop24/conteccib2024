from django.urls import path

from . import views

app_name = 'home'
urlpatterns = [
    path('', views.home, name='home'),
    path('administrator/', views.admin, name='admin'),
    path('participant/', views.participant, name='participant'),
]