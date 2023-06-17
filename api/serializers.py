from django.contrib.auth.models import User
from rest_framework import serializers
from login.models import Attachments

class ProfileSerializer(serializers.Serializer):
   entity_id = serializers.IntegerField()
   profile_image_url = serializers.CharField()

class userSerializer(serializers.ModelSerializer):
    # attachments = ProfileSerializer()
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
