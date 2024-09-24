from django.contrib import admin
from .models import Armario, Emprestimo

@admin.register(Armario)
class ArmarioAdmin(admin.ModelAdmin):
    list_display = ['chave_string', 'disponivel']
    search_fields = ['chave_string', 'disponivel']


@admin.register(Emprestimo)
class EmprestimoAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'armario', 'data_emprestimo']
    search_fields = ['usuario', 'armario', 'data_emprestimo']
    ordering = ['usuario', 'armario', 'data_emprestimo']