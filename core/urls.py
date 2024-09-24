from django.urls import path
from .views import IndexView, MyAccountUpdateView, MyProfileUpdateView, MyProfileView, LivrosPDF, LivrosCreate, LivroUpdate

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    # sessão de usuário
    path('profile/<int:pk>/', MyProfileView.as_view(), name='my_profile'),
    path('profile/<int:pk>/edit_profile/', MyProfileUpdateView.as_view(), name='my_profile_update'),
    path('profile/<int:pk>/edit_account/', MyAccountUpdateView.as_view(), name='my_account_update'),
    # sessão de livros
    path('books/', LivrosPDF.as_view(), name='livros'),
    path('administracao/books/create/', LivrosCreate.as_view(), name='livros_add'),
    path('administracao/book_<int:pk>/update/', LivroUpdate.as_view(), name='livros_update')
]