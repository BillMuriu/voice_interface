from django import forms
from .models import Matter

class MatterForm(forms.ModelForm):
    class Meta:
        model = Matter
        fields = ['title', 'description']
