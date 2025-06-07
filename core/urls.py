from django.urls import path
from .views import IndexView, MyProfileView, LivrosPDF, LivrosCreate, LivroUpdate

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    # sessão de usuário
    path('profile/<int:pk>/', MyProfileView.as_view(), name='my_profile'),
    # sessão de livros
    path('books/', LivrosPDF.as_view(), name='livros'),
    path('administracao/books/create/', LivrosCreate.as_view(), name='livros_add'),
    path('administracao/book_<int:pk>/update/', LivroUpdate.as_view(), name='livros_update')
]