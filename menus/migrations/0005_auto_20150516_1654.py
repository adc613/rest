# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0004_auto_20150516_1514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='restuarant',
            field=models.ForeignKey(related_name='menu', to=settings.AUTH_USER_MODEL),
        ),
    ]
