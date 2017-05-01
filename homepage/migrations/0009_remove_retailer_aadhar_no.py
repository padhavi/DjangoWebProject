# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0008_auto_20170414_1335'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='retailer',
            name='aadhar_no',
        ),
    ]
