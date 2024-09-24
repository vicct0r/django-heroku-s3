from usuarios.models import AlunoModel, ProfessorModel
from .models import Livros
from django import forms

class AlunoUpdateForm(forms.ModelForm):
    class Meta:
        model = AlunoModel
        fields = ['img']


class ProfessorUpdateForm(forms.ModelForm):
    class Meta:
        model = ProfessorModel
        fields = ['img', 'especialidade']


class LivrosModelForm(forms.ModelForm):
    class Meta:
        model = Livros
        fields = ['nome', 'arquivo', 'foto_livro']