# Generated by Django 2.0.6 on 2019-03-05 16:23

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('gameApp', '0003_auto_20190305_1620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamecollector',
            name='dateAccountCreated',
            field=models.DateField(default=datetime.datetime(2019, 3, 5, 16, 23, 44, 771529, tzinfo=utc)),
        ),
    ]
