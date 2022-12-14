# Generated by Django 4.1.3 on 2022-11-20 12:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('historial', models.CharField(max_length=50)),
                ('fecha_ingreso', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=10)),
                ('fecha_nacimiento', models.DateTimeField()),
                ('nombre_usuario', models.CharField(max_length=50)),
                ('Contrasena', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_factura', models.DateTimeField()),
                ('precio', models.IntegerField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ferreteria.cliente')),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ferreteria.empleado')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('tipo', models.CharField(max_length=50)),
                ('existencia', models.IntegerField()),
                ('valor', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_factura', models.DateTimeField()),
                ('cantidad', models.IntegerField()),
                ('valor', models.IntegerField()),
                ('factura', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ferreteria.factura')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ferreteria.producto')),
            ],
        ),
        migrations.AddField(
            model_name='producto',
            name='proveedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ferreteria.proveedor'),
        ),
        migrations.AddField(
            model_name='factura',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ferreteria.producto'),
        ),
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_compra', models.DateTimeField()),
                ('cantidad', models.IntegerField()),
                ('precio', models.IntegerField()),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ferreteria.producto')),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ferreteria.proveedor')),
            ],
        ),
    ]
