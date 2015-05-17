# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('transactions', '0002_auto_20150516_1950'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='menu',
        ),
        migrations.AddField(
            model_name='order',
            name='restuarant',
            field=models.OneToOneField(related_name='host', null=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='order',
            name='waiter',
            field=models.OneToOneField(related_name='waiter', default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='orderer',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
    ]
