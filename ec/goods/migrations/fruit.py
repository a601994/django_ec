# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fruit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=20)),
                ('price', models.FloatField()),
                ('brief', models.CharField(max_length=100)),
                ('detail', models.CharField(max_length=500)),
                ('sold', models.IntegerField(default=0)),
                ('origin', models.CharField(max_length=50)),
            ],
        ),
    ]
