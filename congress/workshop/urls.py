from django.urls import path

from . import views

app_name = 'workshop'
urlpatterns = [
    path('', views.WorkshopListView.as_view(), name='list'),
    path('details/<int:pk>/', views.WorkshopDetailView.as_view(), name='detail'),
    path('create/', views.WorkshopCreateView.as_view(), name='create'),
    path('update/<int:pk>/', views.WorkshopUpdateView.as_view(), name='update'),
]