# Generated by Django 4.1.1 on 2022-10-20 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0010_alter_empleadomeli_cbu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleadomeli',
            name='dni',
            field=models.BigIntegerField(default=0),
        ),
    ]