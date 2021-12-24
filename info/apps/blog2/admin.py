from django.contrib import admin
from .models import *

class PostAdmin(admin.ModelAdmin):
	list_display = ('titulo', 'autor', 'categoria', 'fecha_creacion')
	list_filter = ('fecha_creacion','categoria',)
	search_fields=('autor',)


class ComentarioAdmin(admin.ModelAdmin):
	list_display = ('autor', 'titulo')
	list_filter = ('autor',)
	search_fields=('autor',)
    

admin.site.register(Post, PostAdmin)
admin.site.register(Comentario, ComentarioAdmin)
admin.site.register(Persona)

