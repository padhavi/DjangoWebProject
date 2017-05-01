# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('homepage', '0010_fcomplain'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fcomplain',
            name='f',
        ),
        migrations.AddField(
            model_name='fcomplain',
            name='user',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
        ),
    ]
