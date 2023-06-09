# Generated by Django 3.2.16 on 2023-05-19 01:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('moduloApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bodega',
            options={'verbose_name': 'Bodega', 'verbose_name_plural': 'Bodegas'},
        ),
        migrations.AddField(
            model_name='producto',
            name='bodega',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='moduloApp.bodega'),
        ),
        migrations.AlterField(
            model_name='productobodega',
            name='id_Bodega',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='moduloApp.bodega'),
        ),
        migrations.AlterField(
            model_name='productobodega',
            name='id_Producto',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='moduloApp.producto'),
        ),
    ]
