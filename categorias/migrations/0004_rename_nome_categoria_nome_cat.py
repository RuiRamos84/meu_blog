# Generated by Django 4.1.3 on 2022-11-09 01:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categorias', '0003_rename_nome_cat_categoria_nome'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categoria',
            old_name='nome',
            new_name='nome_cat',
        ),
    ]