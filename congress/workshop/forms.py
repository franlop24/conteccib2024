from django import forms

from .models import Workshop

class WorkshopForm(forms.ModelForm):
    class Meta:
        model = Workshop
        fields = '__all__'
        exclude = ['seats_occupied']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
            'date': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
            'initial_hour': forms.TimeInput(attrs={'type': 'time'}),
            'final_hour': forms.TimeInput(attrs={'type': 'time'}),
        }