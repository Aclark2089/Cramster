# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('paid', models.BooleanField()),
            ],
            options={
                'ordering': ['-order_date'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('product_name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('stock_quantity', models.PositiveSmallIntegerField()),
                ('description', models.CharField(max_length=200)),
                ('active', models.BooleanField()),
            ],
            options={
                'ordering': ['price'],
            },
        ),
        migrations.CreateModel(
            name='ProductOrder',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('quantity', models.PositiveSmallIntegerField()),
                ('order', models.ForeignKey(related_name='products', to='store.Order')),
                ('product', models.ForeignKey(related_name='orders', to='store.Product')),
            ],
        ),
        migrations.CreateModel(
            name='StoreUser',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('address', models.CharField(max_length=100)),
                ('auth_user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('supplier_name', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['supplier_name'],
            },
        ),
        migrations.AddField(
            model_name='product',
            name='supplier',
            field=models.ManyToManyField(to='store.Supplier', related_name='products'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(related_name='orders', to='store.StoreUser'),
        ),
    ]
