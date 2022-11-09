from django.db import models

# Create your models here.
class Categoria(models.Model):
    nome_cat = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.nome_cat