# Generated by Django 4.1.4 on 2022-12-08 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proyectos',
            name='foto',
        ),
        migrations.AddField(
            model_name='proyectos',
            name='archivo_foto',
            field=models.ImageField(default='', upload_to=''),
        ),
        migrations.AddField(
            model_name='proyectos',
            name='url_foto',
            field=models.CharField(default='', max_length=300),
        ),
    ]