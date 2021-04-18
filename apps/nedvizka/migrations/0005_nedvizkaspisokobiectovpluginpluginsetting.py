# Generated by Django 3.0.13 on 2021-04-18 12:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
        ('nedvizka', '0004_nedvizkapanelupravleniapluginsetting'),
    ]

    operations = [
        migrations.CreateModel(
            name='NedvizkaSpisokObiectovPluginPluginSetting',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='nedvizka_nedvizkaspisokobiectovpluginpluginsetting', serialize=False, to='cms.CMSPlugin')),
                ('tip_nedvizki', models.CharField(choices=[('dom_prodaza', 'Дом-продажа'), ('dom_arenda', 'Дом-аренда')], max_length=255, verbose_name='Тип недвижки')),
                ('obiectov_na_stranize', models.IntegerField(default=10, verbose_name='Выводить по ')),
                ('css_class', models.CharField(blank=True, max_length=255, null=True, verbose_name='CSS класс')),
                ('css_style', models.CharField(blank=True, max_length=1000, null=True, verbose_name='CSS стиль')),
            ],
            options={
                'verbose_name': 'Недвижка. Список объектов',
                'verbose_name_plural': 'Недвижка. Список объектов',
            },
            bases=('cms.cmsplugin',),
        ),
    ]