# Generated by Django 3.0.13 on 2021-03-22 12:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
        ('cms', '0022_auto_20180620_1551'),
    ]

    operations = [
        migrations.CreateModel(
            name='SetkaFonovihIzobrazeniiLvSetting',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='setka_fonovih_izobrazenii_setkafonovihizobrazeniilvsetting', serialize=False, to='cms.CMSPlugin')),
                ('css_class', models.CharField(blank=True, max_length=255, null=True, verbose_name='Класс')),
                ('css_style', models.TextField(blank=True, null=True, verbose_name='Стиль')),
            ],
            options={
                'verbose_name': 'Сетка фоновых изображений LV',
                'verbose_name_plural': 'Сетка фоновых изображений LV',
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='SetkaFonovihIzobrazeniiDvSetting',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='setka_fonovih_izobrazenii_setkafonovihizobrazeniidvsetting', serialize=False, to='cms.CMSPlugin')),
                ('zagolovok', models.TextField(default='Заголовок', max_length=255, verbose_name='Заголовок')),
                ('img', filer.fields.image.FilerImageField(on_delete=django.db.models.deletion.CASCADE, to=settings.FILER_IMAGE_MODEL, verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Сетка фоновых изображений DV',
                'verbose_name_plural': 'Сетка фоновых изображений DV',
            },
            bases=('cms.cmsplugin',),
        ),
    ]
