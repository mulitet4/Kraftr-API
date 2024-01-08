from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404

from .serializers import UserSerializer


@api_view(["POST"])
def register(request):
  serializer = UserSerializer(data=request.data)
  if not serializer.is_valid():
    return Response(serializer.errors)
  
  #? This saves the data as well?
  serializer.save()
  user = User.objects.get(username=request.data["username"])
  
  # This hashes the password
  user.set_password(request.data["password"])
  user.save()
  
  token = Token.objects.create(user = user)
  return Response({"token": token})


@api_view(["POST"])
def login(request):
  user = get_object_or_404(User, username=request.data["username"])
  if not user.check_password(request.data["password"]):
    return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
  
  # Create a token if not created already
  token, created = Token.objects.get_or_create(user=user)
  
  # Here we pass in an already 
  # existing instance instead of data.
  # This is for get views.
  serializer = UserSerializer(instance=user)
  return Response({"token": token.key, "user": serializer.data})
