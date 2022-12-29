
from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from .serializer import RegisterSerializer,UserSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import CustomUser
from rest_framework import viewsets


from django.contrib.auth import get_user_model
User = get_user_model()

#class CreateUser(CreateAPIView):
#    queryset = User.objects.all()
#    serializer_class = RegisterSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
