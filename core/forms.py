from .models import Livros
from django import forms

class LivrosModelForm(forms.ModelForm):
    class Meta:
        model = Livros
        fields = ['nome', 'arquivo', 'foto_livro']