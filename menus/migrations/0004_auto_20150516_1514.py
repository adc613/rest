# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0003_auto_20150516_1506'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menu',
            old_name='resturant',
            new_name='restuarant',
        ),
    ]
