# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0007_auto_20170414_1026'),
    ]

    operations = [
        migrations.AddField(
            model_name='fcomplain',
            name='complain',
            field=models.CharField(default='', max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fcomplain',
            name='status_update',
            field=models.CharField(default='', max_length=250),
            preserve_default=False,
        ),
    ]
