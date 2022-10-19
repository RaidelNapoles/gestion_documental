from django.urls import path
from .views import index, home, articulo, articulo_impreso, autor, texto, exportar_articulo_a_txt, search, search_result, administracion, listar_articulos, ArticuloCreateView, ArticuloUpdateView, ArticuloDeleteView

urlpatterns = [
    path('', index, name='index'),
    path('home/', home, name='home'),
    path('pagina-<int:page_number>/', home, name='home'),
    path('articulo/<int:id>/', articulo, name='articulo'),
    path('articulo_impreso/<int:id>/', articulo_impreso, name='articulo_impreso'),
    path('autor/<int:id>/pagina-<int:page_number>/', autor, name='autor'),
    path('texto/', texto, name='texto'),
    path('articulo_a_txt/<int:id>', exportar_articulo_a_txt, name='exportar_a_txt'),

    path('buscar/', search, name='search'),
    path('buscar/pagina-<int:page_number>/',
         search_result, name='search_result'),

    path('administracion/', administracion, name='administracion'),
    path(
        'administracion/articulo/listar/',
        listar_articulos,
        name='articulos_listar'
    ),
    path('administracion/articulo/crear/',
         ArticuloCreateView.as_view(), name='articulos_crear'),
    path('administracion/articulo/<int:pk>/actualizar/',
         ArticuloUpdateView.as_view(), name='articulos_actualizar'),
    path('administracion/articulo/<int:pk>/eliminar/',
         ArticuloDeleteView.as_view(), name='articulos_eliminar'),

]
