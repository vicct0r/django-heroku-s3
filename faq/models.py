from django.db import models
from django.conf import settings


class Pergunta(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    assunto = models.CharField(max_length=50)
    pergunta = models.TextField()
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.assunto} | {self.autor} '


class Resposta(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    resposta = models.TextField()
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.autor} | {self.resposta[:50]}'


