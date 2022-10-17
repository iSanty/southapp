# Generated by Django 4.1.1 on 2022-10-17 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CatPicking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod', models.CharField(max_length=3)),
                ('descripcion', models.CharField(max_length=180)),
            ],
        ),
        migrations.CreateModel(
            name='CatRepo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod', models.CharField(max_length=3)),
                ('descripcion', models.CharField(max_length=180)),
            ],
        ),
        migrations.CreateModel(
            name='CatUbicacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod', models.CharField(max_length=3)),
                ('descripcion', models.CharField(max_length=180)),
            ],
        ),
        migrations.CreateModel(
            name='Cia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod', models.CharField(max_length=3)),
                ('descripcion', models.CharField(max_length=180)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cia', models.CharField(max_length=3)),
                ('codigo', models.CharField(max_length=15)),
                ('descripcion', models.CharField(max_length=180)),
                ('peso_un', models.FloatField(null=0)),
                ('largo_un', models.FloatField(null=0)),
                ('ancho_un', models.FloatField(null=0)),
                ('alto_un', models.FloatField(null=0)),
                ('unidad_caja', models.IntegerField(null=0)),
                ('largo_cj', models.FloatField(null=0)),
                ('ancho_cj', models.FloatField(null=0)),
                ('alto_cj', models.FloatField(null=0)),
                ('unidad_pall', models.IntegerField(null=0)),
                ('pack', models.CharField(max_length=15)),
                ('vd', models.FloatField(null=0)),
                ('tipo_alm', models.CharField(max_length=15)),
                ('fecha_creacion', models.DateTimeField(null=True)),
                ('usuario', models.CharField(max_length=180)),
                ('cat_ub', models.CharField(max_length=3)),
                ('cat_pk', models.CharField(max_length=3)),
                ('cat_repo', models.CharField(max_length=3)),
                ('cat_emb', models.CharField(max_length=3)),
                ('clase', models.CharField(max_length=1)),
                ('unidad_minima', models.IntegerField(null=1)),
                ('unidad_medida', models.CharField(max_length=180, null='01')),
                ('peso_cj', models.FloatField(null=0)),
                ('peso_pall', models.FloatField(null=0)),
                ('largo_pall', models.CharField(max_length=180, null='1,2')),
                ('ancho_pall', models.CharField(max_length=180, null='1')),
                ('alto_pall', models.CharField(max_length=180, null='1,4')),
                ('importado_saad', models.CharField(max_length=2, null='No')),
                ('importado_presis', models.CharField(max_length=2, null='No')),
            ],
        ),
        migrations.CreateModel(
            name='TipoAlm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='TipoPack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=10)),
            ],
        ),
    ]
