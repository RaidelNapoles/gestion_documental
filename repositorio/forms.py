from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from .models import Articulo


class ArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = '__all__'
        widgets = {
            'autores': FilteredSelectMultiple('Autores', False),
            'palabras_claves': FilteredSelectMultiple('Palabras Claves', False),
        }
