# Generated by Django 4.1.1 on 2022-11-29 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='informepreparacion',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
