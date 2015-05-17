# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('transactions', '0004_auto_20150517_1342'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='reservee',
        ),
        migrations.AddField(
            model_name='reservation',
            name='creator',
            field=models.ForeignKey(related_name='reservators', default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='orderer',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='order',
            name='waiter',
            field=models.ForeignKey(related_name='waiter', to=settings.AUTH_USER_MODEL),
        ),
    ]
