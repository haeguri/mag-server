from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)
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

class UserManager(BaseUserManager):
    def create_user(self, email, nickname, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            nickname=nickname,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nickname, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(email,
            password=password,
            nickname=nickname
        )
        # user.is_staff = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

    def exist_email(self, email):
        try:
            User.objects.get(email = email)
            return True
        except:
            return False



class User(AbstractBaseUser, PermissionsMixin):
    email       = models.EmailField('이메일 주소', max_length=255, unique=True, blank=False)
    nickname    = models.CharField('별명',     max_length=20, unique=True, blank=False)

    date_joined = models.DateTimeField('가입일', auto_now_add=True)

    def get_upload_path(instance, filename):
        path = os.path.join("users/%s/[profile]" % instance.nickname, filename)
        return path

    profile_img = models.ImageField('프로필 이미지', upload_to=get_upload_path, blank=True)

    is_active   = models.BooleanField(default=True)

    is_staff    = models.BooleanField("컨텐츠 제작자 여부", default=False,
                                      help_text="자신의 채널, 컨텐츠에 관한 관리 권한을 가집니다.")

    objects     = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nickname',]

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.nickname

    def __str__(self):     # __unicode__ on Python 2
        return self.nickname

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True