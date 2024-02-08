from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, authentication
from rest_framework import status

from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404

from ..products.models import Product

from .models import Cart
from .serializers import UserSerializer, CartSerializer

User=get_user_model()


# ----
# User
# ----
@api_view(["POST"])
def register(request):
  serializer = UserSerializer(data=request.data)
  print(serializer)
  if not serializer.is_valid():
    return Response(serializer.errors)
  
  #? This saves the data as well?
  serializer.save()
  user = User.objects.get(email=request.data["email"])
  
  # This hashes the password
  user.set_password(request.data["password"])
  user.save()
  
  import json
  token = Token.objects.create(user = user)
  return Response({"token": str(token)})


@api_view(["POST"])
def login(request):
  user = get_object_or_404(User, email=request.data["email"])
  if not user.check_password(request.data["password"]):
    return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
  
  # Create a token if not created already
  token, created = Token.objects.get_or_create(user=user)
  
  # Here we pass in an already 
  # existing instance instead of data.
  # This is for get views.
  serializer = UserSerializer(instance=user)
  return Response({"token": token.key, "user": serializer.data})


# ----------
# Cart Views
# ----------
class ListCart(APIView):
  permission_classes = [permissions.IsAuthenticated]
  authentication_classes = (authentication.TokenAuthentication,)

  def get(self, request):
    cart = Cart.objects.get_or_create(user=request.user)[0]
    cart_serializer = CartSerializer(cart)

    return Response({"cart": cart_serializer.data}, status.HTTP_200_OK)

  
@api_view(["POST"])
def addCart(request):
  user_cart = Cart.objects.get_or_create(user=request.user)[0]
  user_cart.cart.add(request.data["id"])
  user_cart.save()

  user_cart_serializer = CartSerializer(user_cart)

  return Response({"cart_details": user_cart_serializer.data})


@api_view(["POST"])
def deleteCart(request, **kwargs):
  user_cart = Cart.objects.get_or_create(user=request.user)[0]
  user_cart.cart.remove(kwargs["id"])
  user_cart.save()

  user_cart_serializer = CartSerializer(user_cart)

  return Response({"cart_details": user_cart_serializer.data})
