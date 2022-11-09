from django.db import models
from categorias.models import Categoria
from posts.models import Post
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.

class Comentario(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    mensagem = models.TextField()
    data = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True)
    post = models.ForeignKey('posts.Post', on_delete=models.CASCADE)
    publidado = models.BooleanField(default=False)

    def __str__(self):
        return self.nome
