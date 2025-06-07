from django.contrib import admin
from .models import Livros

@admin.register(Livros)
class LivrosAdmin(admin.ModelAdmin):
    fields = ['nome', 'arquivo', 'foto_livro']