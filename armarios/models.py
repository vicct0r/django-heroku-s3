from django.db import models
from usuarios.models import CustomUser 
from django.utils import timezone

class Armario(models.Model):
    chave_string = models.CharField('Chave do Armário', max_length=6)
    disponivel = models.BooleanField('Disponivel', default=True)

    def __str__(self):
        return self.chave_string

class Emprestimo(models.Model):
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    armario = models.ForeignKey(Armario, on_delete=models.CASCADE)
    data_emprestimo = models.DateTimeField('Data do Emprestimo', null=True, blank=True)
    data_devolucao = models.DateTimeField('Data de Devolução', null=True, blank=True)


    def __str__(self):
        return f'Armário: {self.id} - Aluno: {self.usuario.username}'

    def emprestar(self):
        self.armario.disponivel = False
        self.data_emprestimo = timezone.now()
        self.armario.save()
        self.save()

    def devolver(self):
        self.armario.disponivel = True
        self.data_devolucao = timezone.now()
        self.armario.save()
        self.save()

    # lembrar de testar isso aqui depois de ter implementado multa no sistema
    def prazo_devolucao(self):
        prazo_limite = self.data_emprestimo + timezone.timedelta(hours=24)
        tempo_restante = prazo_limite - timezone.now()

        if tempo_restante > timezone.timedelta(0):
            dias = tempo_restante.days
            horas, segundos = divmod(tempo_restante.seconds, 3600)
            minutos, segundos = divmod(segundos, 60)
            return f"{dias} dias, {horas} horas, {minutos} minutos"
        else:
            # posso aplicar multa para user aqui dentro.
            return "A devolução está atrasada!"