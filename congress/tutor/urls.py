from django.urls import path

from . import views

app_name = 'tutor'
urlpatterns = [
    path('', views.TutorListView.as_view(), name='list'),
    path('create/', views.create_tutor, name='create'),
]