# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_delete_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='farmer',
            name='aadhar_no',
            field=models.IntegerField(default=0),
        ),
    ]
