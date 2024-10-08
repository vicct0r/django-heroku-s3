from django import forms 
from .models import Pergunta, Resposta

class PerguntaForm(forms.ModelForm):
    class Meta:
        model = Pergunta
        fields = ['assunto', 'pergunta']


class RespostaForm(forms.ModelForm):
    class Meta:
        model = Resposta
        fields = ['resposta']

