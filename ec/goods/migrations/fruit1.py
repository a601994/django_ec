# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', 'fruit'),
    ]

    operations = [
        migrations.AddField(
            model_name='fruit',
            name='is_delete',
            field=models.BooleanField(default=False),
        ),
    ]
