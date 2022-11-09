from django.contrib import admin
from .models import Comentario


class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('id','nome', 'email', 'mensagem', 'data', 'publidado',)
    list_display_links = ('id', 'nome',)
    list_editable = ('publidado',)


admin.site.register(Comentario, ComentarioAdmin)
