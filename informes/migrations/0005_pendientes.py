# Generated by Django 4.1.1 on 2022-11-22 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('informes', '0004_globalpk_nombre_planilla'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pendientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('canal', models.CharField(max_length=100)),
                ('pend_tres_o_mas', models.IntegerField(null=0)),
                ('pend_dos', models.IntegerField(null=0)),
                ('pend_uno', models.IntegerField(null=0)),
                ('base_del_dia', models.IntegerField(null=0)),
                ('finalizado', models.IntegerField(null=0)),
                ('pendiente_para_sig_dia', models.IntegerField(null=0)),
            ],
        ),
    ]
