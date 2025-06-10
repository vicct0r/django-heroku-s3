from django.shortcuts import render, redirect
from .forms import CadastroUsuarioForm, AlunoForm, ProfessorForm, CadastroUsuarioChangeForm, AlunoUpdateForm, ProfessorUpdateForm
from django.views.generic import CreateView, UpdateView, RedirectView, FormView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse_lazy, reverse
from .models import AlunoModel, ProfessorModel
from rolepermissions.roles import assign_role


class LoginRedirectView(LoginRequiredMixin, RedirectView):
    def get_redirect_url(self):
        user = self.request.user

        if user.is_ativo:
            return reverse('index')
        else:
            if user.is_funcionario or user.is_superuser:
                professor = ProfessorModel.objects.get(usuario=user)
                messages.info(self.request, "Informe os seus dados para prosseguir!")
                return reverse('teacher_form', kwargs={'pk':professor.pk})
            else:
                aluno = AlunoModel.objects.get(usuario=user)
                messages.info(self.request, "Informe os seus dados para prosseguir!")
                return reverse('student_form', kwargs={'pk':aluno.pk})


class CadastroUsuarioView(CreateView):
    template_name = 'registration/signup.html'
    form_class = CadastroUsuarioForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        response = super().form_valid(form)
        user = self.object

        if '@' in user.username:
            user.is_funcionario = True
            assign_role(user, 'professor')
            ProfessorModel.objects.create(usuario=user)
        else:
            assign_role(user, 'aluno')
            AlunoModel.objects.create(usuario=user)
        user.save() # preciso disso aqui pra salvar is_funcionario
        
        messages.success(self.request, "Cadastro realizado com sucesso!")
        return response


class StudentFormView(LoginRequiredMixin, UpdateView):
    model = AlunoModel
    template_name = 'usuarios/student_form.html'
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
        messages.info(self.request, "Informações salvas com sucesso!")
        return response


class TeacherFormView(LoginRequiredMixin, FormView):
    model = ProfessorModel
    template_name = 'usuarios/teacher_form.html'
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
        messages.info(self.request, "Informações salvas com sucesso!")
        return response


class ProfileUpdateTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'usuarios/profile_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['user_form'] = CadastroUsuarioChangeForm(instance=user, prefix="user_form")

        if user.is_funcionario:
            instance = ProfessorModel.objects.get(usuario=user)
            context['profile_form'] = ProfessorUpdateForm(instance=instance, prefix="profile_form")
        else:
            instance = AlunoModel.objects.get(usuario=user)
            context['profile_form'] = AlunoUpdateForm(instance=instance, prefix="profile_form")
        
        return context
    
    def post(self, request, *args, **kwargs):
        user = self.request.user
        user_form = CadastroUsuarioChangeForm(request.POST, request.FILES, instance=user, prefix='user_form')
        
        if user.is_funcionario:
            profile = ProfessorModel.objects.get(usuario=user)
            profile_form = ProfessorUpdateForm(request.POST, instance=profile, prefix='profile_form')
        else:
            profile = AlunoModel.objects.get(usuario=user)
            profile_form = AlunoUpdateForm(request.POST, instance=profile, prefix='profile_form')
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(self.request, "Dados alterados com sucesso!")
            return redirect('my_profile', pk=user.pk)
    
        context = {
            "user_form": user_form,
            "profile_form": profile_form
        }

        return render(request, self.template_name, context)