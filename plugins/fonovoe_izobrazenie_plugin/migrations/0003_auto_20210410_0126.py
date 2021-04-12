# Generated by Django 3.0.13 on 2021-04-09 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fonovoe_izobrazenie_plugin', '0002_auto_20210410_0117'),
    ]

    operations = [
        migrations.AddField(
            model_name='fonovoeizobrazeniepluginsetting',
            name='fix_razmer',
            field=models.BooleanField(default=True, verbose_name='Фиксированный размер?'),
        ),
        migrations.AlterField(
            model_name='fonovoeizobrazeniepluginsetting',
            name='crop',
            field=models.BooleanField(default=False, verbose_name='Обрезать?'),
        ),
        migrations.AlterField(
            model_name='fonovoeizobrazeniepluginsetting',
            name='height',
            field=models.PositiveIntegerField(default=900, verbose_name='Высота при сжатие'),
        ),
        migrations.AlterField(
            model_name='fonovoeizobrazeniepluginsetting',
            name='width',
            field=models.PositiveIntegerField(default=1600, verbose_name='Ширина при сжатие'),
        ),
    ]
