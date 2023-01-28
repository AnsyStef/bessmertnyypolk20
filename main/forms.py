from .models import *
from django import forms
from django.forms import ModelForm


class SearchForm(ModelForm):
    class Meta:
        model = Search
        fields = ['search']
        widgets = {'search': forms.TextInput(attrs={'id':'search-form','placeholder':'Фамилия Имя Отчество'})
        }