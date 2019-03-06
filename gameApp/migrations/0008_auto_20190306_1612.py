# Generated by Django 2.0.6 on 2019-03-06 16:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gameApp', '0007_merge_20190306_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamecollector',
            name='userTableForeignKey',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
