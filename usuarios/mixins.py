from .models import AlunoModel, ProfessorModel

class UserProfilePictureMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        if user.is_superuser:
            return context

        if user.is_authenticated:
                if user.is_funcionario:
                    profile = ProfessorModel.objects.get(usuario=user)
                else:
                    profile = AlunoModel.objects.get(usuario=user)
                context['profile'] = profile
        return context