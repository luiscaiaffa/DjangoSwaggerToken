from django.shortcuts import render
from rest import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import permissions, status, generics, mixins
from rest_framework.parsers import MultiPartParser, FormParser
from oauth2_provider.ext.rest_framework import TokenHasReadWriteScope, TokenHasScope, OAuth2Authentication

class UserList(generics.ListAPIView):
	serializer_class = serializers.UserSerializer

	def get_queryset(self):
		queryset = User.objects.all()
		return queryset

class UserListToken(generics.ListAPIView):
	permission_classes = [TokenHasReadWriteScope]
	serializer_class = serializers.UserSerializer

	def get_queryset(self):
		queryset = User.objects.all()
		return queryset
