# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0018_auto_20170416_0404'),
    ]

    operations = [
        migrations.AddField(
            model_name='sell',
            name='crop_pic',
            field=models.FileField(default=1, upload_to=b''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='f_ad_details',
            name='status_update',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='fcomplain',
            name='status_update',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='r_ad_details',
            name='status_update',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='rcomplain',
            name='status_update',
            field=models.BooleanField(default=False),
        ),
    ]
