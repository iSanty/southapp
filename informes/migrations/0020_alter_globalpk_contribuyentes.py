# Generated by Django 4.1.1 on 2023-01-19 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('informes', '0019_globalpk_finalizado_pk_por_globalpk_usuario_inicio_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='globalpk',
            name='contribuyentes',
            field=models.IntegerField(null=True),
        ),
    ]
