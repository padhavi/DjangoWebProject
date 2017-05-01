# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0022_fcomplain_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sell',
            name='crop_pic',
            field=models.FileField(upload_to=b'documents/%Y/%m/%d'),
        ),
    ]
