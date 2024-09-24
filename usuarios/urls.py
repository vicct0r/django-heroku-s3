from django.urls import path
from .views import CadastroUsuarioView, StudentFormView, TeacherFormView, LoginRedirectView
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('', CadastroUsuarioView.as_view(), name='cadastro'),
    path('login/', LoginView.as_view(template_name='login_page.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('student_form/<int:pk>/', StudentFormView.as_view(), name='student_form'),
    path('teacher_form/<int:pk>/', TeacherFormView.as_view(), name='teacher_form'),
    path('redirect/', LoginRedirectView.as_view(), name='redirect')
]