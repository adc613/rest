# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0006_auto_20150517_1416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='cost_of_food',
            field=models.DecimalField(null=True, max_digits=6, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='order',
            name='total_cost',
            field=models.DecimalField(null=True, max_digits=6, decimal_places=2),
        ),
    ]
