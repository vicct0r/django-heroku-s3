from django.urls import path
from .views import EventoListView, EventoDetailView, EventoCreateView, EventoEditView, EventoDeleteView

urlpatterns = [
    path('administracao/', EventoListView.as_view(), name='evento_admin'),
    path('detalhe/<int:pk>/', EventoDetailView.as_view(), name='evento_detalhe'),
    path('administracao/edit_<int:pk>/', EventoEditView.as_view(), name='evento_edit'),
    path('administracao/create_event/', EventoCreateView.as_view(), name='evento_create'),
    path('administracao/delete_<int:pk>/', EventoDeleteView.as_view(), name='evento_delete'),

]