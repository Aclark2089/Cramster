# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20151113_1846'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductOrder',
            fields=[
                ('order_id', models.OneToOneField(to='store.Order', primary_key=True, serialize=False)),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='ordercontent',
            name='order',
        ),
        migrations.RemoveField(
            model_name='ordercontent',
            name='product',
        ),
        migrations.RemoveField(
            model_name='productsupplier',
            name='product',
        ),
        migrations.RemoveField(
            model_name='productsupplier',
            name='supplier',
        ),
        migrations.RemoveField(
            model_name='userorder',
            name='order',
        ),
        migrations.RemoveField(
            model_name='userorder',
            name='user',
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(null=True, to='store.User'),
        ),
        migrations.AddField(
            model_name='supplier',
            name='product',
            field=models.ManyToManyField(to='store.Product'),
        ),
        migrations.DeleteModel(
            name='orderContent',
        ),
        migrations.DeleteModel(
            name='ProductSupplier',
        ),
        migrations.DeleteModel(
            name='userOrder',
        ),
        migrations.AddField(
            model_name='product',
            name='product_order',
            field=models.ForeignKey(null=True, to='store.ProductOrder'),
        ),
    ]
