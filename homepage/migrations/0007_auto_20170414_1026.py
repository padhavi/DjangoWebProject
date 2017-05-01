# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0006_farmer_phone'),
    ]

    operations = [
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
    ]
