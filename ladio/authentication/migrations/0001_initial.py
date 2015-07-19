# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import authentication.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, blank=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(help_text='Designates that this user has all permissions without explicitly assigning them.', default=False, verbose_name='superuser status')),
                ('email', models.EmailField(unique=True, max_length=255, verbose_name='이메일 주소')),
                ('nickname', models.CharField(unique=True, max_length=20, verbose_name='별명')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='가입일')),
                ('profile_img', models.ImageField(upload_to=authentication.models.User.get_upload_path, blank=True, verbose_name='프로필 이미지')),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(help_text='자신의 채널, 컨텐츠에 관한 관리 권한을 가집니다.', default=False, verbose_name='컨텐츠 제작자 여부')),
                ('groups', models.ManyToManyField(related_query_name='user', help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', verbose_name='groups', to='auth.Group', blank=True, related_name='user_set')),
                ('user_permissions', models.ManyToManyField(related_query_name='user', help_text='Specific permissions for this user.', verbose_name='user permissions', to='auth.Permission', blank=True, related_name='user_set')),
            ],
            options={
                'verbose_name_plural': '유저 목록',
                'ordering': ['-date_joined'],
                'verbose_name': '유저',
            },
        ),
    ]
