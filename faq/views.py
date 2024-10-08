from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Pergunta, Resposta
from .forms import PerguntaForm, RespostaForm
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from .models import Pergunta, Resposta
from usuarios.models import AlunoModel, ProfessorModel


class FaqHome(ListView):
    template_name = 'faq_home.html'
    model = Pergunta
    context_object_name = 'perguntas'


class TopicoDetalhe(DetailView):
    model = Pergunta
    template_name = 'faq_detail.html'
    context_object_name = 'pergunta'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Autor da pergunta
        autor_pergunta = self.object.autor  # O campo que referencia o usuário que fez a pergunta
        autor_pergunta_info = self.get_user_info(autor_pergunta)
        context['autor_pergunta_info'] = autor_pergunta_info

        # Respostas
        respostas = Resposta.objects.filter(pergunta=self.object)
        respostas_info = []

        for resposta in respostas:
            autor_resposta = resposta.autor  # O campo que referencia o usuário que fez a resposta
            autor_resposta_info = self.get_user_info(autor_resposta)
            respostas_info.append({
                'resposta_texto': resposta.resposta,  # Campo que armazena o texto da resposta
                'autor_info': autor_resposta_info,
            })

        context['respostas_info'] = respostas_info
        return context

    def get_user_info(self, user):
        """
        Função auxiliar para determinar se o user é aluno ou professor e retornar as informações necessárias.
        """
        try:
            if '@' in user.username:  # Verifica se é professor
                professor = ProfessorModel.objects.get(usuario=user)
                return {
                    'nome_completo': professor.usuario.nome_completo,
                    'img_url': professor.img.url,
                    'tipo': 'Professor',
                }
            else:  # Caso contrário, é aluno
                aluno = AlunoModel.objects.get(usuario=user)
                return {
                    'nome_completo': aluno.usuario.nome_completo,
                    'img_url': aluno.img.url,
                    'tipo': 'Aluno',
                }
        except (AlunoModel.DoesNotExist, ProfessorModel.DoesNotExist):
            # Em caso de falha (não é professor nem aluno), retorna valores padrão
            return {
                'nome_completo': user.username,
                'img_url': 'default/default_user.avif',  # Imagem padrão
                'tipo': 'Usuário Desconhecido',
            }


class FaqPergunta(LoginRequiredMixin, CreateView):
    template_name = 'pergunta_form.html'
    form_class = PerguntaForm
    success_url = reverse_lazy('faq_home')

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pergunta_form'] = self.get_form()
        return context

