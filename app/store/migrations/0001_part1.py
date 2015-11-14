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
                ('order_id', models.AutoField(serialize=False, primary_key=True)),
                ('order_date', models.DateField()),
                ('paid', models.CharField(max_length=1, choices=[('Y', 'Yes'), ('N', 'No')])),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(serialize=False, primary_key=True)),
                ('product_name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('stock_quantity', models.IntegerField()),
                ('description', models.CharField(max_length=200)),
                ('active', models.CharField(max_length=1, choices=[('Y', 'Yes'), ('N', 'No')])),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('supplier_id', models.AutoField(serialize=False, primary_key=True)),
                ('supplier_name', models.CharField(max_length=50)),
                ('product', models.ManyToManyField(to='store.Product')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(serialize=False, primary_key=True)),
                ('user_name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                (***REMOVED***, models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('is_staff', models.CharField(max_length=1, choices=[('Y', 'Yes'), ('N', 'No')])),
            ],
        ),
        migrations.CreateModel(
            name='ProductOrder',
            fields=[
                ('order', models.OneToOneField(serialize=False, primary_key=True, to='store.Order')),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(null=True, to='store.User'),
        ),
        migrations.AddField(
            model_name='product',
            name='product_order',
            field=models.ForeignKey(null=True, to='store.ProductOrder'),
        ),
    ]
