from django.db import models
from categorias.models import Categoria
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.

class Post(models.Model):    
    titulo = models.CharField(max_length=255)
    autor = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    data = models.DateTimeField(default=timezone.now)
    conteudo = models.TextField()
    excerto = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING , blank=True , null=True)
    image = models.ImageField(upload_to='post_img/%Y/%m/%d', blank=True, null=True )
    publicado = models.BooleanField(default=False)


    def __str__(self):
        return self.titulo