# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0005_auto_20150516_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='price',
            field=models.DecimalField(max_digits=6, decimal_places=2),
        ),
    ]
