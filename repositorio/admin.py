from django.contrib import admin
from .models import Autor, Publicacion, Edicion, Articulo, PalabraClave, Seccion, Imagen
from .forms import ArticuloForm
from django.utils.html import format_html

# Register your models here.


class PalabraClaveAdmin(admin.TabularInline):
    autocomplete_fields = ['question']


class ArticuloAdmin(admin.ModelAdmin):
    form = ArticuloForm
    search_fields = [
        'titulo', 'autores__nombre', 'autores__primer_apellido',
        'autores__segundo_apellido', 'texto', 'edicion__publicacion__nombre'
    ]
    list_display = [
        'titulo', 'edicion', 'pagina'
    ]
    # autocomplete_fields = ['palabras_claves']

    def get_form(self, request, obj=None, **kwargs):
        kwargs['form'] = self.form
        return super().get_form(request, obj, **kwargs)


class AutorAdmin(admin.ModelAdmin):
    search_fields = ['nombre', 'primer_apellido', 'segundo_apellido']


class ImagenAdmin(admin.ModelAdmin):
    def image_url(self, obj):
        return format_html('<a href="{}" target="_blank">View Image</a>', obj.image.url)
    image_url.short_description = 'Image URL'


admin.site.register(Autor, AutorAdmin)
admin.site.register(Publicacion)
admin.site.register(Edicion)
admin.site.register(Seccion)
admin.site.register(Articulo, ArticuloAdmin)
admin.site.register(PalabraClave)
admin.site.register(Imagen, ImagenAdmin)

admin.site.site_header = "Administración del sitio"
