# Generated by Django 4.1.1 on 2023-01-31 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('informes', '0027_alter_globalpk_hora_procesado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='globalpk',
            name='hora_fin_armado',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='globalpk',
            name='hora_fin_picking',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='globalpk',
            name='hora_inicio_armado',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='globalpk',
            name='hora_inicio_picking',
            field=models.TimeField(null=True),
        ),
    ]
