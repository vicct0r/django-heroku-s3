from django.shortcuts import render
from django.contrib import messages
from .models import Emprestimo, Armario
from django.views.generic import ListView, View
from usuarios.mixins import UserProfilePictureMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect


class ArmariosView(LoginRequiredMixin, UserProfilePictureMixin, ListView):
    template_name = 'listagem_armarios.html'
    model = Armario

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        
        # O usuario é composição de emprestimo
        # Inserindo 'emprestimo' no context para eu coletar todos emprestimos que user possui.
        emprestimos = Emprestimo.objects.filter(usuario=user)
        context['emprestimos'] = emprestimos
        return context

# Nesta classe precisamos sobrescrever o método 'post'.
# Isso porque estamos usando o método emprestar() e devolver() que foi criado no modelo.
class EmprestimosView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        # O kwargs que eu passei para 'id' é o argumento
        # que a rota recebe para encontrar o objeto especifico.
        user = self.request.user
        armario = get_object_or_404(Armario, id=kwargs['pk'])

        if Emprestimo.objects.filter(usuario=user).exists():
            messages.error(request, 'Você já possui um empréstimo!')
            return redirect('lista_armarios')
        
        emprestimo = Emprestimo.objects.create(
            usuario = request.user,
            armario = armario,
        )
        emprestimo.emprestar()
        messages.success(request, 'Empréstimo realizado com sucesso!')
        return redirect('lista_armarios')


class DevolucaoView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        emprestimo = get_object_or_404(Emprestimo, id=kwargs['pk'])
        emprestimo.devolver()
        emprestimo.delete()
        messages.success(request, 'Devolução realizada com sucesso!')
        return redirect('lista_armarios')