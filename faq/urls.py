from django.urls import path
from .views import FaqHome, FaqPergunta, TopicoDetalhe

urlpatterns = [
    path('home/', FaqHome.as_view(), name='faq_home'),
    path('novo_topico/', FaqPergunta.as_view(), name='faq_pergunta'),
    path('topico/<int:pk>/', TopicoDetalhe.as_view(), name='faq_detalhe')
]