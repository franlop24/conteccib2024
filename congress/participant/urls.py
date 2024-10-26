from django.urls import path

from . import views

app_name = 'participant'
urlpatterns = [
    path('register/', views.ParticipantCreateView.as_view(), name='register'),
    path('list/', views.ParticipantListView.as_view(), name='list'),
    path('detail/<int:pk>/', views.ParticipantDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', views.ParticipantUpdateView.as_view(), name='update'),
    path('validate/<int:pk>/', views.validate_participant, name='validate'),
]