from django.shortcuts import render
from usuarios.models import AlunoModel, CustomUser
from usuarios.mixins import UserProfilePictureMixin
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from rolepermissions.mixins import HasRoleMixin
from armarios.models import Emprestimo
from django.urls import reverse_lazy
from django.contrib import messages
from usuarios.roles import Professor


class AdminProfessores(LoginRequiredMixin, HasRoleMixin, TemplateView):
    allowed_roles = 'professor'
    template_name = 'admin_home.html'


class ListagemAlunos(LoginRequiredMixin, UserProfilePictureMixin, HasRoleMixin, ListView):
    allowed_roles = 'professor'
    template_name = 'lista_alunos.html'
    model = AlunoModel
    context_object_name = 'alunos'


class DetalheAluno(LoginRequiredMixin, UserProfilePictureMixin, HasRoleMixin, DetailView):
    allowed_roles = 'professor'
    template_name = 'detalhe_aluno.html'
    model = AlunoModel
    context_object_name = 'aluno'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        emprestimo = Emprestimo.objects.filter(usuario=user)
        context['emprestimo'] = emprestimo
        return context


class EditarAlunoView(LoginRequiredMixin, UserProfilePictureMixin, HasRoleMixin, UpdateView):
    allowed_roles = 'professor'
    template_name = 'editar_aluno.html'
    model = AlunoModel
    fields = ['curso', 'turno']
    success_url = reverse_lazy('listagem_alunos')

    def form_valid(self, form):
        messages.success(self.request, 'Informações alteradas com sucesso!')
        return super().form_valid(form)


class DeletarAluno(LoginRequiredMixin, HasRoleMixin, DeleteView):
    allowed_roles = 'professor'
    model = AlunoModel
    success_url = reverse_lazy('listagem_alunos')

    def form_valid(self, form):
        messages.success(self.request, 'Usuário removido com sucesso!')
        return super().form_valid(form)