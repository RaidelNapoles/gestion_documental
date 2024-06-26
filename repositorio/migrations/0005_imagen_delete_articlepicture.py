# Generated by Django 4.0.6 on 2024-05-02 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repositorio', '0004_alter_autor_primer_apellido_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Imagen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='pictures/')),
            ],
        ),
        migrations.DeleteModel(
            name='ArticlePicture',
        ),
    ]
