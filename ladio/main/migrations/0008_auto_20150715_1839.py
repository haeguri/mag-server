# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import main.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20150715_0144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel',
            name='bg_img',
            field=models.ImageField(verbose_name='채널 배경화면', help_text='채널의 상세한 정보를 보여주는 페이지에서 배경으로 쓰일 이미지 입니다.', upload_to=main.models.Channel.get_upload_path),
        ),
        migrations.AlterField(
            model_name='channel',
            name='brief',
            field=models.CharField(verbose_name='10글자 소개', max_length=10, help_text='이 채널을 대표할 짧은 문구를 10글자 이내로 적어주세요.'),
        ),
        migrations.AlterField(
            model_name='channel',
            name='ch_name',
            field=models.CharField(verbose_name='채널 이름', max_length=10, help_text='채널의 이름은 무엇인가요?'),
        ),
        migrations.AlterField(
            model_name='channel',
            name='intro',
            field=models.TextField(verbose_name='자기소개', max_length=500, help_text='채널에 대한 소개를 해주세요.'),
        ),
        migrations.AlterField(
            model_name='channel',
            name='user',
            field=models.ForeignKey(verbose_name='채널 발행자', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='content',
            name='body',
            field=models.TextField(verbose_name='본문', help_text='컨텐츠 내용입니다.'),
        ),
        migrations.AlterField(
            model_name='content',
            name='thumb_img',
            field=models.ImageField(verbose_name='썸네일 이미지', help_text='컨텐츠 목록에서 사용자에게 보여질 이미지 입니다.', upload_to=main.models.Content.get_upload_path),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(verbose_name='컨텐츠 제작자 여부', default=False, help_text='자신의 채널, 컨텐츠에 관한 관리 권한을 가집니다.'),
        ),
    ]
