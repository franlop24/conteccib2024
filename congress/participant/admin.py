from django.contrib import admin

from .models import Participant

@admin.register(Participant)
class ParticipantModelAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'workshop']
    list_editable = ['workshop']
