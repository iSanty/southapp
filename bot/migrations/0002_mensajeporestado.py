# Generated by Django 4.1.1 on 2022-12-26 18:07

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MensajePorEstado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(max_length=128)),
                ('mensaje', ckeditor.fields.RichTextField(max_length=256)),
            ],
        ),
    ]