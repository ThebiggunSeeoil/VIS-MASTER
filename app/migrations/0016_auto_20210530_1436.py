# Generated by Django 3.0 on 2021-05-30 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_auto_20210530_1129'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='nozzle',
            options={'ordering': ('log_address', '-pump_log_address'), 'verbose_name': 'มือจ่าย', 'verbose_name_plural': 'ข้อมูลมือจ่าย'},
        ),
    ]
