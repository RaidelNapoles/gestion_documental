from typing import List
from django.contrib import admin
from .models import Autor, Publicacion, Edicion, Articulo, PalabraClave, Seccion

# Register your models here.


class PalabraClaveAdmin(admin.TabularInline):
    autocomplete_fields = ['question']


class ArticuloAdmin(admin.ModelAdmin):
    search_fields = [
        'titulo', 'autores__nombre', 'autores__primer_apellido',
        'autores__segundo_apellido', 'texto', 'edicion__publicacion__nombre'
    ]
    list_display = [
        'titulo', 'edicion', 'pagina'
    ]
    # autocomplete_fields = ['palabras_claves']


class AutorAdmin(admin.ModelAdmin):
    search_fields = ['nombre', 'primer_apellido', 'segundo_apellido']


admin.site.register(Autor, AutorAdmin)
admin.site.register(Publicacion)
admin.site.register(Edicion)
admin.site.register(Seccion)
admin.site.register(Articulo, ArticuloAdmin)
admin.site.register(PalabraClave, PalabraClaveAdmin)

admin.site.site_header = "Administración del sitio"
