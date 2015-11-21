# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_part1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_order',
        ),
        migrations.AddField(
            model_name='productorder',
            name='product',
            field=models.ForeignKey(to='store.Product', null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='stock_quantity',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='productorder',
            name='quantity',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=150),
        ),
    ]
