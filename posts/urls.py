from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.PostIndex.as_view(), name='index'),
    path('categoria/<str:categoria>', views.PostCategoria.as_view() , name='categoria'),
    path('busca/', views.PostBusca.as_view(), name='busca'),
    path('post/<int:id>', views.PostDetalhe.as_view(), name='post'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
