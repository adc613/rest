# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0002_menu_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='resturant',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
