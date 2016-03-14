# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='last_updated_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 11, 16, 15, 26, 756030, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
