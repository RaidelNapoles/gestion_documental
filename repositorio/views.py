from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Articulo, Autor, Publicacion, Edicion, PalabraClave, Texto
from django.conf import settings
from django.db.models import Q
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from bs4 import BeautifulSoup

# Create your views here.
page_size = 4


def index(request):
    autores = Autor.objects.all()
    publicaciones = Publicacion.objects.all()
    return render(request, 'repositorio/index.html', {'autores': autores, 'publicaciones': publicaciones})


def home(request, page_number=1):
    articles = Articulo.objects.all()
    primero = Articulo.objects.dates(
        'edicion__fecha_publicacion', 'year')[0].year
    paginator = Paginator(articles, page_size)
    pages = paginator.num_pages
    pages_to_paginator_display = min(3, pages)
    articles_on_page = paginator.get_page(page_number)
    context = {
        'articulos': articles_on_page,
        'total': articles.count(),
        'pages_to_display': pages_to_paginator_display,
        'primero': primero,
        'home': True,
    }
    return render(request, 'repositorio/home.html', context)


def articulo(request, id):
    articulo = Articulo.objects.get(pk=id)
    texto = articulo.texto
    # parrafos = list(filter(lambda x: x != '', texto.split('\r\n\r\n')))
    context = {
        'articulo': articulo,
        'texto': texto,
        # 'parrafos': parrafos,
    }
    return render(request, 'repositorio/articulo.html', context)


def articulo_impreso(request, id):
    articulo = Articulo.objects.get(pk=id)
    path = settings.MEDIA_URL + articulo.edicion.edicion_impresa.name
    context = {
        'ruta_edicion_impresa': path,
        'pagina': articulo.pagina
    }
    return render(request, 'repositorio/articulo_impreso.html', context)


def autor(request, id, page_number=1):
    autor = Autor.objects.get(pk=id)
    articulos = autor.articulo_set.all()
    query = request.GET.get("buscar")
    if query:
        articulos = Articulo.objects.filter(
            Q(titulo__icontains=query) |
            Q(texto__icontains=query),
            autores__id=id
        ).distinct()
    paginator = Paginator(articulos, page_size)
    articles_on_page = paginator.get_page(page_number)
    context = {
        'autor': autor,
        'articulos': articles_on_page,
        'total': articulos.count()
    }
    return render(request, 'repositorio/autor.html', context)


def texto(request):
    texto = Texto.objects.all()
    return render(request, 'repositorio/texto.html', {'texto': texto})


def exportar_articulo_a_txt(request, id):
    articulo = Articulo.objects.get(pk=id)
    titulo = articulo.titulo
    texto = BeautifulSoup(articulo.texto, "lxml").text
    response = HttpResponse(content_type='application/text charset=utf-8')
    response['Content-Disposition'] = 'attachment; filename="{0}.txt"'.format(
        titulo)
    response.writelines([titulo + '\n\n', texto])
    return response


def search(request):
    autores = Autor.objects.all()
    publicaciones = Publicacion.objects.all()
    return render(request, 'repositorio/search.html', {'autores': autores, 'publicaciones': publicaciones})


def search_result(request, page_number=1):
    autores = Autor.objects.all()
    publicaciones = Publicacion.objects.all()

    general_search = request.GET.get("search", "")
    autor = request.GET.get("inputAuthor", "")
    publicacion = request.GET.get("inputPublication", "")
    titulo = request.GET.get("inputTitle", "")
    keywords = request.GET.get("inputKeywords", "")
    startDate = request.GET.get("startDate", "")
    stopDate = request.GET.get("stopDate", "")
    if general_search or autor or publicacion or titulo or keywords or startDate or stopDate:
        articles = Articulo.objects.all()

        if general_search:
            articles = articles.filter(
                Q(titulo__icontains=general_search) |
                Q(resumen__icontains=general_search) |
                Q(autores__nombre__iexact=general_search) |
                Q(autores__primer_apellido__iexact=general_search) |
                Q(autores__segundo_apellido__iexact=general_search)
            ).distinct()

        if autor:
            nombre = autor.split(' ')[0]
            apellido1 = autor.split(' ')[1]
            apellido2 = autor.split(' ')[2]
            articles = articles.filter(
                Q(autores__nombre=nombre),
                Q(autores__primer_apellido=apellido1),
                Q(autores__segundo_apellido=apellido2),
            )
            # print(str(articles.query))

        if publicacion:
            articles = articles.filter(
                Q(edicion__publicacion__nombre=publicacion)
            )

        if titulo:
            articles = articles.filter(Q(titulo__icontains=titulo))

        if keywords:
            articles = articles.filter(
                Q(palabras_claves__name__icontains=keywords)
            )

        if startDate:
            articles = articles.filter(
                Q(edicion__fecha_publicacion__gte=startDate)
            )

        if stopDate:
            articles = articles.filter(
                Q(edicion__fecha_publicacion__lte=stopDate)
            )

        articles = articles.distinct()
        paginator = Paginator(articles, page_size)
        articles_on_page = paginator.get_page(page_number)
        cleaned_query = {
            key: value for key, value in request.GET.items() if value
        }
        parameters = request.GET.copy()
        context = {
            'articulos': articles_on_page,
            'query': cleaned_query,
            'parameters': parameters,
            'total': articles.count(),
            'home': False,
        }
        return render(request, 'repositorio/home.html', context)

    messages.add_message(
        request, messages.ERROR,
        'Debes rellenar algún campo del formulario de búsqueda.'
    )

    return render(request, 'repositorio/search.html', {'autores': autores, 'publicaciones': publicaciones})


def listar_articulos(request, delete_success=None, create_success=None, article_id=None):
    articles = Articulo.objects.all()
    context = {
        'articulos': articles
    }
    return render(request, 'repositorio/administracion/articulos/articulo_listar.html', context)


def administracion(request):
    return render(request, 'repositorio/administracion/index.html')


class AutorCreateView(CreateView):
    model = Autor
    fields = '__all__'


class AutorUpdateView(UpdateView):
    model = Autor
    fields = '__all__'


class AutorDeleteView(DeleteView):
    model = Autor
    success_url = reverse_lazy('autor')


class PublicacionCreateView(CreateView):
    model = Publicacion
    fields = '__all__'


class PublicacionUpdateView(UpdateView):
    model = Publicacion
    fields = '__all__'


class PublicacionDeleteView(DeleteView):
    model = Publicacion
    success_url = reverse_lazy('autor')


class EdicionCreateView(CreateView):
    model = Edicion
    fields = '__all__'


class EdicionUpdateView(UpdateView):
    model = Edicion
    fields = '__all__'


class EdicionDeleteView(DeleteView):
    model = Edicion
    success_url = reverse_lazy('autor')


class PalabraClaveCreateView(CreateView):
    model = PalabraClave
    fields = '__all__'


class PalabraClaveUpdateView(UpdateView):
    model = PalabraClave
    fields = '__all__'


class PalabraClaveDeleteView(DeleteView):
    model = PalabraClave
    success_url = reverse_lazy('autor')


class ArticuloCreateView(CreateView):
    model = Articulo
    fields = '__all__'
    template_name = 'repositorio/administracion/articulos/articulo_form.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['title_section'] = 'Crear artículo'
        context['updating'] = False
        return context


class ArticuloUpdateView(UpdateView):
    model = Articulo
    fields = '__all__'
    template_name = 'repositorio/administracion/articulos/articulo_form.html'
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['title_section'] = 'Modificar artículo'
        context['updating'] = True
        return context


class ArticuloDeleteView(DeleteView):
    model = Articulo
    template_name = 'repositorio/administracion/articulos/articulo_confirm_delete.html'
    context_object_name = 'article'

    def get_success_url(self) -> str:
        return reverse_lazy('articulos_listar')
