# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20150715_1839'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='channel',
            options={'ordering': ['-created']},
        ),
        migrations.AlterModelOptions(
            name='content',
            options={'ordering': ['-created']},
        ),
        migrations.AlterModelOptions(
            name='channel',
            options={'verbose_name': ['채널']},
        ),
        migrations.AlterModelOptions(
            name='channel',
            options={'verbose_name_plural': ['채널 목록']},
        ),
        migrations.AlterModelOptions(
            name='content',
            options={'verbose_name': ['컨텐츠']},
        ),
        migrations.AlterModelOptions(
            name='content',
            options={'verbose_name_plural': ['컨텐츠 목록']},
        ),
    ]
