from django.urls import path

from . import views

app_name = 'participant'
urlpatterns = [
    path('register/', views.ParticipantCreateView.as_view(), name='register'),
    path('list/', views.ParticipantListView.as_view(), name='list'),
    path('validate/<int:pk>/', views.validate_participant, name='validate'),
]