# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import main.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('email', models.EmailField(unique=True, verbose_name='이메일 주소', max_length=255)),
                ('nickname', models.CharField(unique=True, verbose_name='별명', max_length=20)),
                ('date_joined', models.DateTimeField(verbose_name='가입일', auto_now_add=True)),
                ('profile_img', models.ImageField(verbose_name='프로필 이미지', blank=True, upload_to=main.models.User.get_upload_path)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(verbose_name='관리자', default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('ch_name', models.CharField(verbose_name='채널 이름', max_length=10)),
                ('bg_img', models.ImageField(verbose_name='채널 배경화면', upload_to=main.models.Channel.get_upload_path)),
                ('brief', models.CharField(verbose_name='10글자 소개', max_length=10)),
                ('intro', models.TextField(verbose_name='자기소개', max_length=500)),
                ('created', models.DateTimeField(verbose_name='생성일', auto_now_add=True)),
                ('user', models.ForeignKey(verbose_name='채널을 만드는 사람', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('title', models.CharField(verbose_name='컨텐츠 제목', max_length=20)),
                ('thumb_img', models.ImageField(verbose_name='썸네일 이미지', upload_to=main.models.Content.get_upload_path)),
                ('body', models.TextField(verbose_name='본문')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('channel', models.ForeignKey(verbose_name='발행 채널', to='main.Channel')),
            ],
        ),
    ]
