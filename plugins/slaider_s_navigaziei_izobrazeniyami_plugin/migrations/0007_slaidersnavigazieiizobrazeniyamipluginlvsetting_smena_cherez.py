# Generated by Django 3.0.13 on 2021-04-23 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slaider_s_navigaziei_izobrazeniyami_plugin', '0006_slaidersnavigazieiizobrazeniyamipluginlvsetting_speed'),
    ]

    operations = [
        migrations.AddField(
            model_name='slaidersnavigazieiizobrazeniyamipluginlvsetting',
            name='smena_cherez',
            field=models.IntegerField(default=3000, verbose_name='Смсена слайда через (мс)'),
        ),
    ]
