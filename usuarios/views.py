from django.shortcuts import render
from .forms import CadastroUsuarioForm, AlunoForm, ProfessorForm, CadastroUsuarioChangeForm
from django.views.generic import CreateView, UpdateView, RedirectView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
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

        if '@' in user.username or user.is_superuser:
            user.is_funcionario = True
            assign_role(user, 'professor')
            ProfessorModel.objects.create(usuario=user)
        else:
            assign_role(user, 'aluno')
            AlunoModel.objects.create(usuario=user)
        
        messages.success(self.request, "Cadastro realizado com sucesso!")
        user.save() # preciso disso aqui pra salvar is_funcionario
        return response


class StudentFormView(LoginRequiredMixin, UserProfilePictureMixin, FormView):
    model = AlunoModel
    template_name = 'student_account_update.html'
    form_class = AlunoForm
    success_url = reverse_lazy('index')

    def get_object(self):
        user = self.request.user
        return AlunoModel.objects.get(usuario=user)
    
    def post(self, request, *args, **kwargs):
        form1 = self.get_form()
        form2 = CadastroUsuarioChangeForm(request.POST)

        if form1.is_valid() and form2.is_valid():
            return self.form_valid(form1, form2)
        else:
            return self.form_invalid(form1, form2)
        
    def form_valid(self, form1, form2):
        data1 = form1.cleaned_data
        data2 = form2.cleaned_data
        return super().form_valid(form1)
    
    def form_invalid(self, form1, form2):
        return self.render_to_response(self.get_context_data(form=form1, form2=form2))


class TeacherFormView(LoginRequiredMixin, UserProfilePictureMixin, FormView):
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
        messages.info(self.request, "Informações salvas com sucesso!")
        user.save()
        return response