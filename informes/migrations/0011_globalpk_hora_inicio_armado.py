# Generated by Django 4.1.1 on 2023-01-17 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('informes', '0010_globalpk_iniciado_por'),
    ]

    operations = [
        migrations.AddField(
            model_name='globalpk',
            name='hora_inicio_armado',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
