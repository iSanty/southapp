# Generated by Django 4.1.1 on 2022-10-20 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0005_empleadomeli_alias_empleadomeli_banco_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sucursal', models.CharField(max_length=10)),
            ],
        ),
    ]
