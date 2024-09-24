from django.urls import path
from .views import ArmariosView, EmprestimosView, DevolucaoView

urlpatterns = [
    path('', ArmariosView.as_view(), name='lista_armarios'),
    path('emprestimo/<int:pk>/', EmprestimosView.as_view(), name='emprestimo_armario'),
    path('devolver/<int:pk>/', DevolucaoView.as_view(), name='devolver')
]