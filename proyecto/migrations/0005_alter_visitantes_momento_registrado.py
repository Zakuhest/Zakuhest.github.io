# Generated by Django 4.1.4 on 2022-12-09 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto', '0004_visitantes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitantes',
            name='momento_registrado',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]