# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel',
            name='bg_img',
            field=models.ImageField(help_text='채널의 상세한 정보를 보여주는 페이지에서 배경으로 쓰일 이미지 입니다.', upload_to=main.models.Channel.get_upload_path, verbose_name='채널 배경화면', max_length=500),
        ),
        migrations.AlterField(
            model_name='content',
            name='thumb_img',
            field=models.ImageField(help_text='컨텐츠 목록에서 사용자에게 보여질 이미지 입니다.', upload_to=main.models.Content.get_upload_path, verbose_name='썸네일 이미지', max_length=500),
        ),
    ]
