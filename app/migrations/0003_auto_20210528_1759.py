# Generated by Django 3.0 on 2021-05-28 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20210528_1758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nozzle',
            name='pump_log_address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
