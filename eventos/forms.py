from django import forms
from .models import Evento

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['nome', 'descricao', 'data', 'local', 'duracao', 'status', 'logo']
        widgets = {
            'data': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'duracao': forms.TimeInput(attrs={'type': 'time'}),
        }