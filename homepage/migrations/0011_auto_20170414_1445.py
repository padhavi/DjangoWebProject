# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0010_auto_20170414_1337'),
    ]

    operations = [
        migrations.AddField(
            model_name='farmer',
            name='phone',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='farmer',
            name='aadhar_no',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='retailer',
            name='phone',
            field=models.IntegerField(),
        ),
    ]
