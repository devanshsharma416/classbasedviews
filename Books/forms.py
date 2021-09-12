from django import forms
from django.db import models
from django.forms import Form, fields, widgets
from .models import Books

class AddForm(forms.ModelForm):

    class Meta:
        model = Books
        fields = ('title', 'genre', 'author', 'isbn')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'genre': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'isbn': forms.TextInput(attrs={'class': 'form-control'}),
        }
    