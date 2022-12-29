from django.contrib.auth.models import User
from rest_framework import serializers
from django.core.mail import EmailMessage
from .models import CustomUser
from django.contrib.auth import get_user_model

User = get_user_model()



        
    

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['email'], validated_data['password'])
        email = EmailMessage(
        'Title',
        (validated_data['email']),
        'my-email',
        ['my-receive-email']
        )
        email.send()
       
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}


