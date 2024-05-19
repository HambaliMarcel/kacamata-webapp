from django import forms
from .models import Materi

class MateriForm(forms.ModelForm):
    class Meta:
        model = Materi
        fields = ['title', 'description', 'grade', 'file']
