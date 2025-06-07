from django.contrib import admin
from .models import Evento

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'status', 'descricao', 'local', 'data', 'duracao', 'logo']