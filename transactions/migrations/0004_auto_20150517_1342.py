# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0003_auto_20150517_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='restuarant',
            field=models.ForeignKey(related_name='host', to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='reservee',
            field=models.OneToOneField(related_name='reservee', to=settings.AUTH_USER_MODEL),
        ),
    ]
