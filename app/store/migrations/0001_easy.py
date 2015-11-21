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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('order_date', models.DateField(auto_now_add=True)),
                ('quantity', models.PositiveSmallIntegerField()),
                ('paid', models.CharField(max_length=1, choices=[('Y', 'Yes'), ('N', 'No')])),
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
                ('active', models.CharField(max_length=1, choices=[('Y', 'Yes'), ('N', 'No')])),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('supplier_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('user_name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                (***REMOVED***, models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=150)),
                ('is_staff', models.CharField(max_length=1, choices=[('Y', 'Yes'), ('N', 'No')])),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='supplier',
            field=models.ManyToManyField(related_name='products', to='store.Supplier'),
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ForeignKey(to='store.Product', related_name='orders'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(to='store.User', related_name='orders'),
        ),
    ]
