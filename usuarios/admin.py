from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, ProfessorModel, AlunoModel
from .forms import CadastroUsuarioForm, CadastroUsuarioChangeForm

@admin.register(AlunoModel)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'curso']


@admin.register(ProfessorModel)  
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'especialidade']


@admin.register(CustomUser)
class UsuarioCustomUserAdmin(UserAdmin):
    add_form = CadastroUsuarioForm
    form = CadastroUsuarioChangeForm
    model = CustomUser
    list_display = ['username', 'nome_completo', 'is_ativo', 'multado']