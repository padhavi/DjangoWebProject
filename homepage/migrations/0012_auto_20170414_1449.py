# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0011_auto_20170414_1445'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='crop',
            name='cropid',
        ),
        migrations.AddField(
            model_name='crop',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, default=1, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
