# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import main.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('ch_name', models.CharField(help_text='채널의 이름은 무엇인가요?', max_length=10, verbose_name='채널 이름')),
                ('bg_img', models.ImageField(help_text='채널의 상세한 정보를 보여주는 페이지에서 배경으로 쓰일 이미지 입니다.', upload_to=main.models.Channel.get_upload_path, verbose_name='채널 배경화면')),
                ('brief', models.CharField(help_text='이 채널을 대표할 짧은 문구를 10글자 이내로 적어주세요.', max_length=10, verbose_name='10글자 소개')),
                ('intro', models.TextField(help_text='채널에 대한 소개를 해주세요.', max_length=500, verbose_name='자기소개')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='생성일')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='채널 발행자')),
            ],
            options={
                'verbose_name_plural': '채널 목록',
                'ordering': ['-created'],
                'verbose_name': '채널',
            },
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=20, verbose_name='컨텐츠 제목')),
                ('thumb_img', models.ImageField(help_text='컨텐츠 목록에서 사용자에게 보여질 이미지 입니다.', upload_to=main.models.Content.get_upload_path, verbose_name='썸네일 이미지')),
                ('body', models.TextField(help_text='컨텐츠 내용입니다.', verbose_name='본문')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('channel', models.ForeignKey(to='main.Channel', verbose_name='발행 채널')),
            ],
            options={
                'verbose_name_plural': '컨텐츠 목록',
                'ordering': ['-created'],
                'verbose_name': '컨텐츠',
            },
        ),
    ]
