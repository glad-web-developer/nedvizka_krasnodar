# Generated by Django 3.0.13 on 2021-04-17 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('svoi_stili_i_scripti_plugin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='svoistiliscriptpluginsetting',
            name='text',
            field=models.TextField(blank=True, null=True, verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='svoistiliscriptpluginsetting',
            name='type',
            field=models.CharField(choices=[('style', 'Стиль'), ('script', 'Скрипт')], default='div', max_length=30, verbose_name='Тип'),
        ),
    ]