from rest_framework import serializers

from main.models import Content, Channel

class ChannelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Channel

class ContentSerializer(serializers.ModelSerializer):

    created = serializers.DateTimeField(format='%Y-%m-%d %H:%M')

    class Meta:
        model = Content