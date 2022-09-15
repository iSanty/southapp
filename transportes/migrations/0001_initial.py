# Generated by Django 4.1.1 on 2022-09-15 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transportes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dominio', models.CharField(max_length=30)),
                ('nombre', models.CharField(max_length=15)),
                ('apellido', models.CharField(max_length=15)),
                ('imagen1', models.ImageField(blank=True, null=True, upload_to='camionetas')),
                ('imagen2', models.ImageField(blank=True, null=True, upload_to='camionetas')),
                ('imagen3', models.ImageField(blank=True, null=True, upload_to='camionetas')),
                ('imagen4', models.ImageField(blank=True, null=True, upload_to='camionetas')),
                ('imagen5', models.ImageField(blank=True, null=True, upload_to='camionetas')),
                ('imagen6', models.ImageField(blank=True, null=True, upload_to='camionetas')),
                ('imagen7', models.ImageField(blank=True, null=True, upload_to='camionetas')),
            ],
        ),
    ]