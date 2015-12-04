# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['price']},
        ),
        migrations.AlterField(
            model_name='order',
            name='paid',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='active',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(),
        ),
    ]
