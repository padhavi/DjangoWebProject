# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0020_fcomplain_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fcomplain',
            name='user',
        ),
        migrations.AlterField(
            model_name='fcomplain',
            name='f',
            field=models.ForeignKey(blank=True, to='homepage.farmer', null=True),
        ),
    ]
