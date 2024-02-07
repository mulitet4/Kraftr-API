from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Cart
from ..products.serializers import ProductSerializer

User=get_user_model()

class UserSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = User
    fields = ["id", "email", "password"]

class CartSerializer(serializers.ModelSerializer):
  cart = ProductSerializer('cart', many=True)
  class Meta:
    model = Cart
    fields = ["id", "user", "cart"]