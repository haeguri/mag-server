# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20150716_0153'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='channel',
            options={'verbose_name': '채널', 'verbose_name_plural': '채널 목록', 'ordering': ['-created']},
        ),
        migrations.AlterModelOptions(
            name='content',
            options={'verbose_name': '컨텐츠', 'verbose_name_plural': '컨텐츠 목록', 'ordering': ['-created']},
        ),
    ]
