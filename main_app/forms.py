from django import forms
from .models import CareLog

class CareLogForm(forms.ModelForm):
    class Meta:
        model = CareLog
        fields = ['activity', 'notes', 'date']
        widgets = {
            'date': forms.DateInput(
                format='%Y-%m-%d',
                attrs={
                    'type': 'date',
                    'class': 'form-control'
                }
            ),
            'notes': forms.Textarea(attrs={
                'rows': 3,
                'class': 'materialize-textarea'
            }),
            'activity': forms.Select(attrs={
                'class': 'form-control'
            })
        }