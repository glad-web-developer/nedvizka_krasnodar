# Generated by Django 3.0.13 on 2021-05-31 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nedvizka', '0005_auto_20210531_1112'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='domarenda',
            name='nomer',
        ),
        migrations.RemoveField(
            model_name='domprodaza',
            name='nomer',
        ),
        migrations.AddField(
            model_name='domarenda',
            name='adres',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Адрес'),
        ),
        migrations.AddField(
            model_name='domprodaza',
            name='adres',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Адрес'),
        ),
    ]
