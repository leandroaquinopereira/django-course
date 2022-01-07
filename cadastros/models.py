from django.db import models

# Create your models here.

class Pais(models.Model):

    nome = models.CharField(max_length=80, unique=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'País'
        verbose_name_plural = 'Países'

class Estado(models.Model):

    pais = models.ForeignKey(Pais, on_delete=models.PROTECT) # CASCADE - deleta; SET_NULL - seta o pais dos estados para null; PROTECT - nao deixa excluir enquanto tiver estado vinculado
    nome = models.CharField(max_length=80)

    def __str__(self):
        return self.nome

class Cidade(models.Model):

    estado = models.ForeignKey(Estado, on_delete=models.PROTECT, null=True, blank=False)
    nome = models.CharField(max_length=100, unique=True)
    capital = models.BooleanField(default=False, help_text='Check')

    def __str__(self):
        return self.nome

