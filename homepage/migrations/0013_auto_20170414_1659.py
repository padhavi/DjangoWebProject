# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0012_auto_20170414_1449'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='crop',
            name='id',
        ),
        migrations.AddField(
            model_name='crop',
            name='cropid',
            field=models.AutoField(default=1, serialize=False, primary_key=True),
            preserve_default=False,
        ),
    ]
