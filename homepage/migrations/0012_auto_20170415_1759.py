# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0011_auto_20170415_1757'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fcomplain',
            name='user',
        ),
        migrations.AddField(
            model_name='fcomplain',
            name='f',
            field=models.ForeignKey(default=1, to='homepage.farmer'),
            preserve_default=False,
        ),
    ]
