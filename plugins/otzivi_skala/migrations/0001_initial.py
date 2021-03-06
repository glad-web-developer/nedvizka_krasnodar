# Generated by Django 3.0.13 on 2021-05-31 02:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
    ]

    operations = [
        migrations.CreateModel(
            name='OtziviSkalaDvPluginSetting',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='otzivi_skala_otziviskaladvpluginsetting', serialize=False, to='cms.CMSPlugin')),
                ('avtor', models.CharField(blank=True, max_length=255, null=True, verbose_name='Автор')),
                ('img', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Превью автора')),
                ('opisanie', models.TextField(blank=True, null=True, verbose_name='Отзыв')),
                ('data', models.DateField(blank=True, null=True, verbose_name='Дата')),
                ('ssilla', models.CharField(blank=True, max_length=500, null=True, verbose_name='Ссылка')),
                ('nazvanie_otzivnika', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название отзывника')),
            ],
            options={
                'verbose_name': 'Отзывы - слайд',
                'verbose_name_plural': 'Отзывы - слайды',
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='OtziviSkalaLvPluginSetting',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='otzivi_skala_otziviskalalvpluginsetting', serialize=False, to='cms.CMSPlugin')),
            ],
            options={
                'verbose_name': 'Отзывы слайдер',
                'verbose_name_plural': 'Отзывы слайдеры',
            },
            bases=('cms.cmsplugin',),
        ),
    ]
