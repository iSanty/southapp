# Generated by Django 4.1.1 on 2022-11-14 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('informes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='globalpk',
            name='fecha_armado',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='globalpk',
            name='fecha_picking',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='globalpk',
            name='fecha_procesado',
            field=models.DateTimeField(null=True),
        ),
    ]