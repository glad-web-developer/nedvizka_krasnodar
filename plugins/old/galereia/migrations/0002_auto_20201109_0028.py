# Generated by Django 3.0.10 on 2020-11-08 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galereia', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='galereialvnaglavnoipluginsetting',
            name='img_phone',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Изображение для телефона'),
        ),
        migrations.AlterField(
            model_name='galereialvnaglavnoipluginsetting',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Изображение для PC'),
        ),
    ]
