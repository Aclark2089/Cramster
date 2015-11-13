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
                ('order_date', models.DateField()),
                ('paid', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='orderContent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('quantity', models.IntegerField()),
                ('order', models.ManyToManyField(to='store.Order')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.DateField()),
                ('price', models.IntegerField()),
                ('stock_quantity', models.IntegerField()),
                ('description', models.CharField(max_length=200)),
                ('active', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='productSupplied',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('product', models.ManyToManyField(to='store.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('supplier_id', models.AutoField(primary_key=True, serialize=False)),
                ('supplier_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                (***REMOVED***, models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('is_staff', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='userOrder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('order', models.ManyToManyField(to='store.Order')),
                ('user', models.ForeignKey(to='store.User')),
            ],
        ),
        migrations.AddField(
            model_name='productsupplied',
            name='supplier',
            field=models.ManyToManyField(to='store.Supplier'),
        ),
        migrations.AddField(
            model_name='ordercontent',
            name='product',
            field=models.ManyToManyField(to='store.Product'),
        ),
    ]
