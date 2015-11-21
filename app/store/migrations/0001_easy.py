# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_date', models.DateField(auto_now_add=True)),
                ('paid', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('stock_quantity', models.PositiveSmallIntegerField()),
                ('description', models.CharField(max_length=200)),
                ('active', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='ProductOrder',
            fields=[
                ('product_order_id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.PositiveSmallIntegerField()),
                ('order', models.ForeignKey(related_name='contains', to='store.Order', null=True)),
                ('product', models.OneToOneField(related_name='product_order_number', to='store.Product', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('supplier_id', models.AutoField(primary_key=True, serialize=False)),
                ('supplier_name', models.CharField(max_length=50)),
                ('product', models.ManyToManyField(related_name='supplies', to='store.Product')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                (***REMOVED***, models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=150)),
                ('is_staff', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], max_length=1)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(related_name='orders', to='store.User', null=True),
        ),
    ]
