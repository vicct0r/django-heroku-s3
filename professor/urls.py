from django.urls import path
from .views import ListagemAlunos, DetalheAluno, EditarAlunoView, DeletarAluno, AdminProfessores

urlpatterns = [
    path('', ListagemAlunos.as_view(), name='listagem_alunos'),
    path('administracao/alunos/_<int:pk>/detalhe/', DetalheAluno.as_view(), name='detalhe_aluno'),
    path('administracao/alunos/_<int:pk>/', EditarAlunoView.as_view(), name='editar_aluno'),
    path('administracao/alunos/_<int:pk>/delete/', DeletarAluno.as_view(), name='deletar_aluno'),
    path('home/', AdminProfessores.as_view(), name='admin_home'),
]