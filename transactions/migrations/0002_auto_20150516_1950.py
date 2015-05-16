# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0006_auto_20150516_1908'),
        ('transactions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('extras', models.TextField()),
                ('menu_item', models.ForeignKey(to='menus.MenuItem')),
            ],
        ),
        migrations.RemoveField(
            model_name='order',
            name='menu_items',
        ),
        migrations.AddField(
            model_name='order',
            name='cost_of_food',
            field=models.DecimalField(default=1.0, max_digits=6, decimal_places=2, blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='total_cost',
            field=models.DecimalField(default=1.0, max_digits=6, decimal_places=2, blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(related_name='ordered_item', to='transactions.Order'),
        ),
    ]
