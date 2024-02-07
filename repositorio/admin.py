from django.contrib import admin
from .models import Autor, Publicacion, Edicion, Articulo, PalabraClave, Seccion
from .forms import ArticuloForm

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


admin.site.register(Autor, AutorAdmin)
admin.site.register(Publicacion)
admin.site.register(Edicion)
admin.site.register(Seccion)
admin.site.register(Articulo, ArticuloAdmin)
admin.site.register(PalabraClave)

admin.site.site_header = "Administración del sitio"
