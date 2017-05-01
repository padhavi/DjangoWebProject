# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0005_farmer_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='farmer',
            name='id',
        ),
        migrations.RemoveField(
            model_name='farmer',
            name='user',
        ),
        migrations.AddField(
            model_name='farmer',
            name='f_id',
            field=models.AutoField(default=1, serialize=False, primary_key=True),
        ),
    ]
