# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0005_auto_20150517_1351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='tip',
            field=models.DecimalField(null=True, max_digits=6, decimal_places=2),
        ),
    ]
