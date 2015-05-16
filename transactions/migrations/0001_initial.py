# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('menus', '0006_auto_20150516_1908'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tip', models.DecimalField(max_digits=6, decimal_places=2)),
                ('menu', models.ForeignKey(to='menus.Menu')),
                ('menu_items', models.ManyToManyField(to='menus.MenuItem')),
                ('orderer', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.DateTimeField()),
                ('reservee', models.ForeignKey(related_name='reservee', to=settings.AUTH_USER_MODEL)),
                ('restuarant', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
