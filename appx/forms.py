from django import forms
from .models import Student
from django.core.validators import MinValueValidator, MaxValueValidator

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['project_name', 'project_stage', 'project_desc']
        labels = {
            'project_name': 'Project Name',
            'project_stage': 'Project Stage',
            'project_desc': 'Project Description',
        }
        widgets = {
            'project_name': forms.TextInput(attrs={'class': 'form-control'}),
            'project_stage': forms.TextInput(attrs={'class': 'form-control'}),
            'project_desc': forms.TextInput(attrs={'class': 'form-control'}),\
        }
 
