# Generated by Django 4.1.1 on 2023-01-17 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0004_grupomsj'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClienteAtendido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_cel', models.CharField(max_length=20)),
                ('nivel_satisfaccion', models.IntegerField()),
                ('guia_consultada', models.CharField(max_length=12)),
                ('estado_de_guia_consultada', models.CharField(max_length=100)),
            ],
        ),
    ]
