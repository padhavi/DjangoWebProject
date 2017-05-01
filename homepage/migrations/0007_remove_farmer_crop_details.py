# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0006_auto_20170413_0227'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='farmer',
            name='crop_details',
        ),
    ]
