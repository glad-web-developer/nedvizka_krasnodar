# Generated by Django 3.0.13 on 2021-04-18 11:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
        ('nedvizka', '0002_auto_20210418_1933'),
    ]

    operations = [
        migrations.CreateModel(
            name='NedvizkaIzbranoePluginSetting',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='nedvizka_nedvizkaizbranoepluginsetting', serialize=False, to='cms.CMSPlugin')),
                ('css_class', models.CharField(blank=True, max_length=255, null=True, verbose_name='CSS класс')),
                ('css_style', models.CharField(blank=True, max_length=1000, null=True, verbose_name='CSS стиль')),
            ],
            options={
                'verbose_name': 'Недвижка. Избранное',
                'verbose_name_plural': 'Недвижка. Избранное',
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.AlterModelOptions(
            name='fotodomov',
            options={'verbose_name': 'Фото дома', 'verbose_name_plural': 'Фото дома'},
        ),
    ]
