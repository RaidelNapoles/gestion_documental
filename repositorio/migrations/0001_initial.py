# Generated by Django 4.0.6 on 2022-07-13 18:53

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArticlePicture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='article_pictures/')),
            ],
        ),
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('primer_apellido', models.CharField(max_length=100)),
                ('segundo_apellido', models.CharField(blank=True, default='', max_length=100)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='author_pictures/')),
                ('biography', models.TextField(blank=True, default='')),
            ],
            options={
                'verbose_name_plural': 'Autores',
                'ordering': ['primer_apellido'],
            },
        ),
        migrations.CreateModel(
            name='PalabraClave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Publicacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Publicación',
                'verbose_name_plural': 'Publicaciones',
            },
        ),
        migrations.CreateModel(
            name='Texto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='titulo', max_length=100)),
                ('texto', tinymce.models.HTMLField()),
            ],
        ),
        migrations.CreateModel(
            name='Edicion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.PositiveIntegerField()),
                ('fecha_publicacion', models.DateField()),
                ('edicion_impresa', models.FileField(upload_to='newspapers/')),
                ('publicacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='repositorio.publicacion')),
            ],
            options={
                'verbose_name': 'Edición',
                'verbose_name_plural': 'Ediciones',
                'ordering': ['numero'],
            },
        ),
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('seccion', models.IntegerField(blank=True, null=True)),
                ('pagina', models.PositiveIntegerField()),
                ('resumen', models.CharField(blank=True, default='', max_length=400)),
                ('texto', tinymce.models.HTMLField()),
                ('autores', models.ManyToManyField(to='repositorio.autor')),
                ('edicion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='repositorio.edicion')),
                ('palabras_claves', models.ManyToManyField(to='repositorio.palabraclave')),
            ],
            options={
                'verbose_name': 'Artículo',
                'verbose_name_plural': 'Artículos',
                'ordering': ['titulo'],
            },
        ),
    ]
