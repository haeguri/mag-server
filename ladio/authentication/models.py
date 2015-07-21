import os
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)

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

    profile_img = models.ImageField('프로필 이미지', upload_to=get_upload_path, blank=True, max_length=500)

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


    class Meta:
        verbose_name = "유저"
        verbose_name_plural = "유저 목록"
        ordering = ['-date_joined']