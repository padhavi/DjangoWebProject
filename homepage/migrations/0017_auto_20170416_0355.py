# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0016_retailer_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='rcomplain',
            name='complain',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rcomplain',
            name='status_update',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
    ]
