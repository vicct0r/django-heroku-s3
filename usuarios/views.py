from django.shortcuts import render
from .forms import CadastroUsuarioForm, AlunoForm, ProfessorForm
from django.views.generic import CreateView, UpdateView, RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from .models import AlunoModel, ProfessorModel
from .mixins import UserProfilePictureMixin
from rolepermissions.roles import assign_role


class LoginRedirectView(LoginRequiredMixin, RedirectView):
    def get_redirect_url(self):
        user = self.request.user

        if user.is_ativo:
            return reverse('index')
        else:
            if user.is_funcionario:
                professor = ProfessorModel.objects.get(usuario=user)
                return reverse('teacher_form', kwargs={'pk':professor.pk})
            else:
                aluno = AlunoModel.objects.get(usuario=user)
                return reverse('student_form', kwargs={'pk':aluno.pk})


class CadastroUsuarioView(CreateView):
    template_name = 'cadastro.html'
    form_class = CadastroUsuarioForm
    success_url = reverse_lazy('index')


class StudentFormView(LoginRequiredMixin, UserProfilePictureMixin, UpdateView):
    model = AlunoModel
    template_name = 'student_form.html'
    form_class = AlunoForm
    success_url = reverse_lazy('index')

    def get_object(self):
        user = self.request.user
        return AlunoModel.objects.get(usuario=user)
    
    def form_valid(self, form):
        response = super().form_valid(form)
        user = self.request.user
        user.is_ativo = True
        user.save()
        return response


class TeacherFormView(LoginRequiredMixin, UserProfilePictureMixin, UpdateView):
    model = ProfessorModel
    template_name = 'teacher_form.html'
    form_class = ProfessorForm
    success_url = reverse_lazy('index')

    def get_object(self):
        user = self.request.user
        return ProfessorModel.objects.get(usuario=user)

    def form_valid(self, form):
        response = super().form_valid(form)
        user = self.request.user
        user.is_ativo = True
        user.save()
        return response