# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0005_farmer_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='farmer',
            name='phone',
            field=models.IntegerField(default=0),
        ),
    ]
