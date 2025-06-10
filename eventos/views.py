from django.shortcuts import render
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from rolepermissions.mixins import HasRoleMixin
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import EventoForm
from .models import Evento


class EventoDetailView(LoginRequiredMixin, DetailView):
    template_name = 'eventos/evento_detail.html'
    model = Evento
    context_object_name = 'evento'


class EventoListView(LoginRequiredMixin, ListView):
    template_name = 'eventos/evento_admin.html'
    model = Evento
    context_object_name = 'eventos'


class EventoCreateView(LoginRequiredMixin, HasRoleMixin, CreateView):
    allowed_roles = 'professor'
    template_name = 'eventos/evento_create.html'
    form_class = EventoForm
    success_url = reverse_lazy('evento_admin')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Evento criado com sucesso!')
        return response


class EventoEditView(LoginRequiredMixin, HasRoleMixin, UpdateView):
    allowed_roles = 'professor'
    queryset = Evento.objects.all()
    template_name = 'eventos/evento_update.html'
    form_class = EventoForm
    success_url = reverse_lazy('evento_admin')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Evento editado com sucesso!')
        return response


class EventoDeleteView(LoginRequiredMixin, HasRoleMixin, DeleteView):
    allowed_roles = 'professor'
    model = Evento
    success_url = reverse_lazy('evento_admin')

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        messages.success(self.request, 'Evento removido do banco de dados!')
        return response