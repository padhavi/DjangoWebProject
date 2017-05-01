# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('homepage', '0007_remove_farmer_crop_details'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='farmer',
            name='f_id',
        ),
        migrations.AddField(
            model_name='farmer',
            name='crop_details',
            field=models.ForeignKey(default=1, to='homepage.crop'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='farmer',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, default=1, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='farmer',
            name='user',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='retailer',
            name='aadhar_no',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='retailer',
            name='phone',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='retailer',
            name='user',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='retailer',
            name='address',
            field=models.CharField(default=b'abc', max_length=500),
        ),
    ]
