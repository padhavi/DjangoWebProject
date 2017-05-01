# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_product'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Product',
        ),
    ]
