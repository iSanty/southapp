# Generated by Django 4.1.1 on 2022-10-19 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='masdatosusuario',
            name='sucursal',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
