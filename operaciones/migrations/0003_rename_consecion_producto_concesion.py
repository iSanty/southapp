# Generated by Django 4.1.1 on 2022-12-02 18:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operaciones', '0002_producto_consecion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='consecion',
            new_name='concesion',
        ),
    ]
