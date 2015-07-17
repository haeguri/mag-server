from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers, exceptions

from django.contrib.auth import get_user_model, authenticate

from rest_auth.serializers import TokenSerializer as OriginTokenSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth import update_session_auth_hash

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)
    confirm_password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = User
        fields = ('id', 'email', 'nickname', 'date_joined', 'profile_img', 'is_staff',
                  'password', 'confirm_password',)
        read_only_fields = ('created')

        def create(self, validated_data):
            return User.objects.create(**validated_data)

        def update(self, instance, validated_data):
            instance.nickname = validated_data.get('nickname', instance.nickname)

            instance.save()

            password = validated_data.get('password', None)
            confirm_password = validated_data.get('confirm_password', None)

            # 테스트 목적 코
            if password and confirm_password and password == confirm_password:
                instance.set_password(password)
                instance.save()

            update_session_auth_hash(self.context.get('request'), instance)

            return instance



class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'nickname', 'date_joined')


class TokenSerializer(OriginTokenSerializer):
    user = UserDetailsSerializer(many=False)

    class Meta:
        model = Token
        fields = ('key', 'user')

class AuthTokenSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(email=email, password=password)

            if user:
                if not user.is_active:
                    msg = _('User account is disabled.')
                    raise exceptions.ValidationError(msg)
            else:
                msg = _('Unable to log in with provided credentials.')
                raise exceptions.ValidationError(msg)
        else:
            msg = _('Must include "email" and "password"')
            raise exceptions.ValidationError(msg)

        attrs['user'] = user
        return attrs


# 커스텀 AuthTokenSerializer를 상속받음.
class LoginSerializer(AuthTokenSerializer):

    def validate(self, attrs):
        attrs = super(LoginSerializer, self).validate(attrs)
        if 'rest_auth.auth' in settings.INSTALLED_APPS:
            from allauth.account import app_settings

            if app_settings.EMAIL_VERIFICATION == app_settings.EmailVerificationMethod.MANDATORY:
                user = attrs['user']
                email_address = user.emailaddress_set.get(email=user.email)
                if not email_address.verified:
                    raise serializers.ValidationError('E-mail is not verified.')
        return attrs
