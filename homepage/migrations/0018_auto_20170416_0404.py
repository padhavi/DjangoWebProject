# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0017_auto_20170416_0355'),
    ]

    operations = [
        migrations.AddField(
            model_name='f_ad_details',
            name='status_update',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='qty',
            name='price',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='qty',
            name='q',
            field=models.IntegerField(default=23),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='r_ad_details',
            name='status_update',
            field=models.CharField(default=23, max_length=250),
            preserve_default=False,
        ),
    ]
