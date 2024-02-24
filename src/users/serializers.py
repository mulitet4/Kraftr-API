from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import *
from ..products.serializers import ProductSerializer

User=get_user_model()

class UserSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = User
    fields = ["id", "email", "password"]


class CartItemSerializer(serializers.ModelSerializer):
  product = ProductSerializer('product')

  class Meta:
    model = CartItem
    fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
  cart_items = CartItemSerializer('cart_items', many=True)

  class Meta:
    model = Cart
    fields = ["id", "user", "cart_items"]