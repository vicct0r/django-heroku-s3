from django.db import models
from stdimage import StdImageField
from django.core.exceptions import ValidationError

def validar_pdf(value):
    if not value.name.endswith('.pdf'):
        raise ValidationError('O arquivo deve ser um PDF.')
        
class Livros(models.Model):
    nome = models.CharField('Nome do Livro', max_length=60)
    arquivo = models.FileField('Arquivo PDF', upload_to='livros/', validators=[validar_pdf])
    foto_livro = StdImageField(
        upload_to=('books/'),
        variations={'thumb':{'width':200, 'height':200, 'crop':True}}, 
        default=None,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Livro'
        verbose_name_plural = 'Livros'
    
    