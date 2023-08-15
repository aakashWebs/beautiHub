from django.contrib.auth.models import User
from rest_framework import serializers
from login.models import Attachments
from gallery.models import Profile

class ProfileSerializer(serializers.Serializer):
   entity_id = serializers.IntegerField()
   profile_image_url = serializers.CharField()

class userSerializer(serializers.ModelSerializer):
    # attachments = ProfileSerializer()
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class profileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        # fields = '__all__'
        fields = ['id','name','age','description']
class userLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.IntegerField()
