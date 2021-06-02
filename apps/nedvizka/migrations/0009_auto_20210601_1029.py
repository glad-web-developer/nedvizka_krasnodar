# Generated by Django 3.0.13 on 2021-06-01 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nedvizka', '0008_auto_20210601_1018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domarenda',
            name='pokazivat',
            field=models.BooleanField(choices=[(True, 'Показывать'), (False, 'Скрыть')], default=True, verbose_name='Показывать'),
        ),
        migrations.AlterField(
            model_name='domprodaza',
            name='akzia',
            field=models.BooleanField(default=False, verbose_name='Акция/спец цена'),
        ),
        migrations.AlterField(
            model_name='domprodaza',
            name='pokazivat',
            field=models.BooleanField(choices=[(True, 'Показывать'), (False, 'Скрыть')], default=True, verbose_name='Показывать/скрыть'),
        ),
        migrations.AlterField(
            model_name='domprodaza',
            name='price_itogovaia',
            field=models.FloatField(blank=True, null=True, verbose_name='Цена для поиска'),
        ),
    ]