# Generated by Django 3.0 on 2019-12-12 16:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_categoria', models.CharField(max_length=30)),
                ('estado', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='UnidadMedida',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_unidad', models.CharField(max_length=30)),
                ('estado', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_producto', models.CharField(max_length=30)),
                ('cantidad', models.CharField(max_length=3)),
                ('estado', models.BooleanField(default=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='MateriaPrima',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_materi_prima', models.CharField(max_length=40)),
                ('cantidad', models.CharField(max_length=3)),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('estado', models.BooleanField(default=True)),
                ('unidad_medida', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.UnidadMedida')),
            ],
        ),
    ]