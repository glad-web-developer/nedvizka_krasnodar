# Generated by Django 3.0.13 on 2021-06-01 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nedvizka', '0007_auto_20210601_1016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domarenda',
            name='akzia',
            field=models.BooleanField(default=False, editable=False, verbose_name='Акция/спец цена'),
        ),
    ]