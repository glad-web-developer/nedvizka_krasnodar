# Generated by Django 3.0.13 on 2021-03-28 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video_player_js', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='videoplayerjspluginsetting',
            name='css_class',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Класс'),
        ),
        migrations.AddField(
            model_name='videoplayerjspluginsetting',
            name='css_style',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Стиль'),
        ),
        migrations.AddField(
            model_name='videoplayerjspluginsetting',
            name='height',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Высота'),
        ),
        migrations.AddField(
            model_name='videoplayerjspluginsetting',
            name='width',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Ширина'),
        ),
    ]
