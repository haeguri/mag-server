from django.db import models
from datetime import datetime
from django.conf import settings

import os


class Channel(models.Model):

    def get_upload_path(instance, filename):
        path = os.path.join("users/%s/channel_%s/[bg]_%s" % (instance.user.nickname , instance.ch_name, filename))
        return path

    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="채널 발행자", blank=False, null=False)

    ch_name = models.CharField("채널 이름", max_length=10, blank=False
                                        , help_text="채널의 이름은 무엇인가요?")
    bg_img = models.ImageField("채널 배경화면", blank=False, upload_to=get_upload_path
                                        , help_text="채널의 상세한 정보를 보여주는 페이지에서 배경으로 쓰일 이미지 입니다.")
    brief = models.CharField("10글자 소개", max_length=10, blank=False
                                        , help_text="이 채널을 대표할 짧은 문구를 10글자 이내로 적어주세요.")
    intro = models.TextField("자기소개", max_length=500, blank=False\
                                        ,help_text="채널에 대한 소개를 해주세요.")
    created = models.DateTimeField("생성일", auto_now_add=True)

    def __str__(self):
        return self.ch_name

    class Meta:
        verbose_name = "채널"
        verbose_name_plural = "채널 목록"
        ordering = ["-created"]

class Content(models.Model):
    channel = models.ForeignKey(Channel, verbose_name="발행 채널", blank=False, null=False)
    title = models.CharField("컨텐츠 제목", max_length=20)

    def get_upload_path(instance, filename):
        path = os.path.join("users/%s/channel_%s/contents/%s/%s" %
                            (instance.channel.user.nickname, instance.channel.ch_name, datetime.now().strftime('%Y%m%d'), instance.title), "[thumbnail]" + filename)
        return path

    thumb_img = models.ImageField("썸네일 이미지",upload_to=get_upload_path
                                  , help_text="컨텐츠 목록에서 사용자에게 보여질 이미지 입니다.")
    body = models.TextField("본문", blank=False
                                  , help_text="컨텐츠 내용입니다.")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "컨텐츠"
        verbose_name_plural = "컨텐츠 목록"
        ordering = ['-created']


    def __str__(self):
        return self.title