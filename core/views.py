from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import OperationalError
from armarios.models import Emprestimo
from django.views.generic import TemplateView, UpdateView, DetailView, ListView, CreateView
from usuarios.forms import CadastroUsuarioChangeForm
from rolepermissions.mixins import HasRoleMixin
from usuarios.mixins import UserProfilePictureMixin
from eventos.models import Evento
from .models import Livros
from .forms import LivrosModelForm
from django.urls import reverse, reverse_lazy
from usuarios.models import ProfessorModel, AlunoModel, CustomUser
from .forms import ProfessorUpdateForm, AlunoUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin


class IndexView(UserProfilePictureMixin, TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['eventos'] = Evento.objects.all()
        except OperationalError:
            context['eventos'] = []
        
        return context


# Sessão de Usuário
class MyProfileView(LoginRequiredMixin, UserProfilePictureMixin, DetailView):
    template_name = 'my_profile.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        context['emprestimo'] = Emprestimo.objects.filter(usuario=user)

        if user.is_funcionario:
            profile = ProfessorModel.objects.get(usuario=user)
        else:
            profile = AlunoModel.objects.get(usuario=user)
    
        context['profile'] = profile
        return context

    def get_object(self):
        return self.request.user


class MyAccountUpdateView(LoginRequiredMixin, UserProfilePictureMixin, UpdateView):
    template_name = 'my_account_update.html'
    form_class = CadastroUsuarioChangeForm

    def get_object(self):
        return self.request.user

    def form_valid(self, form):
        messages.success(self.request, 'Informações da conta alteradas com sucesso!')
        return super().form_valid(form)
    
    def get_success_url(self):
        # Obtenha o pk do usuário atualizado
        user_pk = self.object.pk
        return reverse('my_profile', kwargs={'pk': user_pk})


class MyProfileUpdateView(LoginRequiredMixin, UserProfilePictureMixin, UpdateView):
    template_name = 'my_profile_update.html'
    success_url = reverse_lazy('my_profile')
    # form_class está fora desta parte pois eu preciso de uma condição para escolher o formulário.

    def get_form_class(self):
        user = self.request.user

        # fazendo os dois retornos possíveis de formulário
        if user.is_funcionario:
            return ProfessorUpdateForm
        return AlunoUpdateForm

    def get_object(self):
        user = self.request.user # retornando o usuario logado

        # especificando o usuário correto para alteração dos dados
        if user.is_funcionario:
            return ProfessorModel.objects.get(usuario=user)
        return AlunoModel.objects.get(usuario=user)

        # get(usuario=user) permite com que eu encontre o usuário correto dentro do meu perfil;
        # a lógica funciona desta forma porque eu fiz com que usuario fosse uma composição de perfil,
        # desta forma eu consigo encontrar o objeto relacionado com a conta de usuario sem nenhum problema.

    def form_valid(self, form):
        messages.success(self.request, 'Informações de perfil alterados com sucesso!')
        return super().form_valid(form)

    def get_success_url(self):
        user_pk = self.object.pk
        return reverse('my_profile', kwargs={'pk': user_pk})

# Sessão de Livros
class LivrosPDF(ListView):
    template_name = 'livros.html'
    model = Livros
    context_object_name = 'livros'


class LivrosCreate(LoginRequiredMixin, HasRoleMixin, CreateView):
    allowed_roles = 'professor'
    template_name = 'livro_add.html'
    form_class = LivrosModelForm
    success_url = reverse_lazy('livros')


class LivroUpdate(LoginRequiredMixin, HasRoleMixin, UpdateView):
    allowed_roles = 'professor'
    template_name = 'livro_update.html'
    queryset = Livros.objects.all()
    form_class = LivrosModelForm
    success_url = reverse_lazy('livros')