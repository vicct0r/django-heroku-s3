from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import OperationalError
from armarios.models import Emprestimo
from django.views.generic import TemplateView, FormView, DetailView, ListView, CreateView, UpdateView
from usuarios.forms import CadastroUsuarioChangeForm
from rolepermissions.mixins import HasRoleMixin
from eventos.models import Evento
from .models import Livros
from .forms import LivrosModelForm
from django.urls import reverse, reverse_lazy
from usuarios.models import ProfessorModel, AlunoModel, CustomUser
from django.contrib.auth.mixins import LoginRequiredMixin


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['eventos'] = Evento.objects.all()
        except OperationalError:
            context['eventos'] = []
        
        return context


# Sessão de Usuário
class MyProfileView(LoginRequiredMixin, DetailView):
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