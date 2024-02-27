from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, authentication
from rest_framework import status

from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404

from ..products.models import Product

from .models import *
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

# TODO Implement adding or reducing quantity
# TODO Make a quantity endpoint to reduce by number
  
# Let this logic remain as it is 
@api_view(["POST"])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def addCart(request):
  user_cart = Cart.objects.get_or_create(user=request.user)[0]
  product_id = request.data["id"]
  
  to_add_item = Product.objects.get(id=product_id)

  if len(user_cart.cart_items.filter(product=to_add_item)) == 0:
    new_cart_item = CartItem.objects.create(product=to_add_item, quantity=1, user=request.user)
    user_cart.cart_items.add(new_cart_item)
    user_cart.save()
  
  else:
    cart_item: CartItem = user_cart.cart_items.get(product=to_add_item)
    cart_item.quantity += 1
    cart_item.save()

  user_cart = Cart.objects.get_or_create(user=request.user)[0]

  user_cart_serializer = CartSerializer(user_cart)

  return Response({"cart": user_cart_serializer.data})


@api_view(["POST"])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def changeCartQuantity(request):
  user_cart = Cart.objects.get_or_create(user=request.user)[0]
  product_id = request.data["id"]
  quantity = request.data["quantity"]
  
  to_change_item = Product.objects.get(id=product_id)

  if len(user_cart.cart_items.filter(product=to_change_item)) == 0:
    new_cart_item = CartItem.objects.create(product=to_change_item, quantity=quantity, user=request.user)
    user_cart.cart_items.add(new_cart_item)
    user_cart.save()
  
  else:
    cart_item: CartItem = user_cart.cart_items.get(product=to_change_item)
    cart_item.quantity = quantity
    cart_item.save()

  user_cart = Cart.objects.get(user=request.user)[0]

  user_cart_serializer = CartSerializer(user_cart)

  return Response({"cart": user_cart_serializer.data})


@api_view(["POST"])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def deleteCart(request, **kwargs):
  user_cart = Cart.objects.get_or_create(user=request.user)[0]
  product_id = request.data["id"]
  
  to_delete_item = Product.objects.get(id=product_id)

  cart_item: CartItem = user_cart.cart_items.delete(product=to_delete_item)

  user_cart_serializer = CartSerializer(user_cart)

  return Response({"cart": user_cart_serializer.data})
