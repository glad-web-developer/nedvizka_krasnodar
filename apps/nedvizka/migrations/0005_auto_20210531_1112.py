# Generated by Django 3.0.13 on 2021-05-31 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nedvizka', '0004_auto_20210530_2036'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='domarenda',
            name='ploshad_uchastka',
        ),
        migrations.RemoveField(
            model_name='domprodaza',
            name='ploshad_uchastka',
        ),
        migrations.AlterField(
            model_name='domarenda',
            name='obshaia_ploshad',
            field=models.FloatField(blank=True, null=True, verbose_name='Плоащдь участка и дома (кв. м)'),
        ),
        migrations.AlterField(
            model_name='domprodaza',
            name='obshaia_ploshad',
            field=models.FloatField(blank=True, null=True, verbose_name='Площадь участка и дома (кв. м)'),
        ),
    ]
