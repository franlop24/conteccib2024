from django.urls import path

from . import views

app_name = 'participant'
urlpatterns = [
    path('register/', views.ParticipantCreateView.as_view(), name='register'),
]