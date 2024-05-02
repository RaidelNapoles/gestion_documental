from django.db import models
from datetime import date
from django.urls import reverse
from tinymce.models import HTMLField

# Create your models here.


class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    primer_apellido = models.CharField(max_length=100, null=True, blank=True)
    segundo_apellido = models.CharField(max_length=100, null=True, blank=True)
    picture = models.ImageField(
        upload_to='author_pictures/', null=True, blank=True)
    biography = models.TextField(default='', blank=True)

    class Meta:
        verbose_name_plural = 'Autores'
        ordering = ['primer_apellido']

    def __str__(self) -> str:
        if self.nombre and self.primer_apellido and self.segundo_apellido:
            return "{primer_apellido} {segundo_apellido}, {nombre}".format(
                nombre=self.nombre,
                primer_apellido=self.primer_apellido,
                segundo_apellido=self.segundo_apellido
            )
        elif self.nombre and self.primer_apellido:
            return "{primer_apellido}, {nombre}".format(
                nombre=self.nombre,
                primer_apellido=self.primer_apellido
            )
        else:
            return self.nombre  # caso especial para las instituciones


class Publicacion(models.Model):
    nombre = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Publicación'
        verbose_name_plural = 'Publicaciones'
        ordering = ['nombre']

    def __str__(self) -> str:
        return self.nombre


class Edicion(models.Model):
    publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE)
    numero = models.PositiveIntegerField()
    fecha_publicacion = models.DateField()
    edicion_impresa = models.FileField(upload_to='newspapers/')

    class Meta:
        verbose_name = 'Edición'
        verbose_name_plural = 'Ediciones'
        ordering = ['numero']

    def __str__(self) -> str:
        return "{publicacion}, no. {numero}, {fecha_publicacion}".format(
            publicacion=self.publicacion,
            fecha_publicacion=self.fecha_publicacion,
            numero=self.numero
        )


class PalabraClave(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')

    class Meta:
        verbose_name = 'Palabra Clave'
        verbose_name_plural = 'Palabras Claves'
        ordering = ['name']

    def __str__(self) -> str:
        return self.name


class Seccion(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')

    class Meta:
        verbose_name = 'Sección'
        verbose_name_plural = 'Secciones'

    def __str__(self) -> str:
        return self.name


class Articulo(models.Model):
    titulo = models.CharField(max_length=200)
    autores = models.ManyToManyField(Autor)
    edicion = models.ForeignKey(Edicion, on_delete=models.CASCADE)
    seccion = models.ForeignKey(
        Seccion, on_delete=models.SET_DEFAULT, null=True, blank=True,
        default=""
    )
    pagina = models.PositiveIntegerField()
    palabras_claves = models.ManyToManyField(PalabraClave)
    resumen = models.TextField(max_length=400, blank=True, default='')
    texto = HTMLField()

    class Meta:
        verbose_name = 'Artículo'
        verbose_name_plural = 'Artículos'
        ordering = ['titulo']

    def get_absolute_url(self):
        return reverse('articulo', kwargs={'id': self.id})

    def __str__(self) -> str:
        return self.titulo

    def get_year_of_pub(self):
        self.edicion.fecha_publicacion


class Imagen(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='pictures/', null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Imágenes'

    def __str__(self) -> str:
        return self.nombre


class Texto(models.Model):
    title = models.CharField(max_length=100, default='titulo')
    texto = HTMLField()

    def __str__(self) -> str:
        return self.title
