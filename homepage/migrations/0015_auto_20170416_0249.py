# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0014_merge'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='retailer',
            name='user',
        ),
        migrations.AlterField(
            model_name='farmer',
            name='aadhar_no',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='retailer',
            name='address',
            field=models.CharField(max_length=500),
        ),
    ]
