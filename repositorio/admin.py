from django.contrib import admin
from .models import Autor, Publicacion, Edicion, Articulo, Texto, PalabraClave, ArticlePicture

# Register your models here.


class ArticuloAdmin(admin.ModelAdmin):
    search_fields = ['titulo', 'autores__nombre', 'autores__primer_apellido',
                     'autores__segundo_apellido', 'texto', 'edicion__publicacion__nombre']
    list_display = ['titulo', 'edicion', 'pagina']


class AutorAdmin(admin.ModelAdmin):
    search_fields = ['nombre', 'primer_apellido', 'segundo_apellido']


admin.site.register(Autor, AutorAdmin)
admin.site.register(Publicacion)
admin.site.register(Edicion)
admin.site.register(Articulo, ArticuloAdmin)
admin.site.register(Texto)
admin.site.register(PalabraClave)
admin.site.register(ArticlePicture)

admin.site.site_header = "Administración del sitio"
