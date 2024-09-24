from django.db import models
from django.conf import settings 
from stdimage import StdImageField

class Evento(models.Model):
    STATUS_CHOICES = (
        ('ativo', 'Ativo'),
        ('cancelado', 'Cancelado'),
        ('finalizado', 'Finalizado'),
    )
    
    
    nome = models.CharField('Nome do Evento', max_length=30, db_index=True)
    status = models.CharField('Status', max_length=10, choices=STATUS_CHOICES, default='ativo', db_index=True)
    descricao = models.TextField('Descrição')
    local = models.CharField('Local', max_length=100, null=True, blank=True)
    data = models.DateTimeField('Data do evento')
    duracao = models.TimeField('Duração', help_text='Ex: 2 horas e 30 minutos')
    palestrantes = models.ManyToManyField(settings.AUTH_USER_MODEL, verbose_name='Palestrante', default=None, blank=True)
    logo = StdImageField(
            upload_to='evento_logos/', 
            variations={'thumb':{'width':250, 'height':250, 'crop':True}}, 
            default=None,
            blank=True,
            null=True
        )
    
    def __str__(self):
        return self.nome