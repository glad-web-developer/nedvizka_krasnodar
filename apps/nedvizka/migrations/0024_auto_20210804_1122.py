# Generated by Django 3.0.13 on 2021-08-04 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nedvizka', '0023_auto_20210804_1055'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fotodomarenda',
            name='dom',
        ),
        migrations.RemoveField(
            model_name='fotodomarenda',
            name='img',
        ),
        migrations.RemoveField(
            model_name='panoramidomaarenda',
            name='dom',
        ),
        migrations.RemoveField(
            model_name='panoramidomprodaza',
            name='dom',
        ),
        migrations.RemoveField(
            model_name='videodomarendda',
            name='dom',
        ),
        migrations.RemoveField(
            model_name='videodomprodaza',
            name='dom',
        ),
        migrations.RemoveField(
            model_name='domprodaza',
            name='ploshad_osnovnogo_doma',
        ),
        migrations.RemoveField(
            model_name='uchactkiarenda',
            name='obshaia_ploshad',
        ),
        migrations.RemoveField(
            model_name='uchactkiprodaza',
            name='obshaia_ploshad',
        ),
        migrations.AlterField(
            model_name='domprodaza',
            name='obshaia_ploshad',
            field=models.FloatField(blank=True, null=True, verbose_name='Площадь дома (кв. м)'),
        ),
        migrations.AlterField(
            model_name='domprodaza',
            name='ploshad_uchastka',
            field=models.FloatField(blank=True, null=True, verbose_name='Площадь участка (кв. м'),
        ),
        migrations.DeleteModel(
            name='DomArenda',
        ),
        migrations.DeleteModel(
            name='FotoDomArenda',
        ),
        migrations.DeleteModel(
            name='PanoramiDomaArenda',
        ),
        migrations.DeleteModel(
            name='PanoramiDomProdaza',
        ),
        migrations.DeleteModel(
            name='VideoDomArendda',
        ),
        migrations.DeleteModel(
            name='VideoDomProdaza',
        ),
    ]
