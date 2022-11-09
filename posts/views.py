from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView 
from django.views.generic.edit import UpdateView
from posts.models import Post

class PostIndex(ListView):
    model = Post
    template_name = 'posts/index.html'
    

class PostBusca(PostIndex):
    pass

class PostCategoria(PostIndex):
    pass

class PostDetalhe(UpdateView):
    pass   