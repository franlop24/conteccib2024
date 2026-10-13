from django.urls import path

from . import views

app_name = 'workshop'
urlpatterns = [
    path('', views.WorkshopListView.as_view(), name='list'),
    path('<int:pk>/details/', views.WorkshopDetailView.as_view(), name='detail'),
    path('create/', views.WorkshopCreateView.as_view(), name='create'),
    path('<int:pk>/update/', views.WorkshopUpdateView.as_view(), name='update'),
    path('<int:pk>/participant/register/', views.workshop_register, name='participant_register'),
    path('instructors/', views.InstructorListView.as_view(), name='instructor_list'),
    path('instructors/create/', views.create_instructor, name='instructor_create'),
    path('instructors/<int:pk>/update/', views.InstructorUpdateView.as_view(), name='instructor_update'),
]
