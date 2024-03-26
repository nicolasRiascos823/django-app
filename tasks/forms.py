from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'important']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'New task...'}),
            'description': forms.Textarea(attrs={'class': 'form-control mb-3', 'placeholder': 'Description task...','rows':'4'}),
            'important': forms.CheckboxInput(attrs={'class': 'mb-3'})
        }