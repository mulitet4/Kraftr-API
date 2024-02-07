from rest_framework import serializers
from .models import *

# depth = 1
# inline serializers


class ShoeSizeSerializer(serializers.ModelSerializer):
  class Meta:
    model = ShoeSize
    fields = ['id', 'shoe_size_type', 'size']


class ShoeTypeSerializer(serializers.ModelSerializer):
  class Meta:
    model = ShoeType
    fields = ['id', 'name']


class PhotoInlineSerializer(serializers.ModelSerializer):
  class Meta:
    model = Photo
    fields = ['id', 'image', 'name']


class ShoeSerializer(serializers.ModelSerializer):
  shoe_sizes = ShoeSizeSerializer('shoe_sizes', many=True)
  shoe_type = ShoeTypeSerializer('shoe_type')
  images = PhotoInlineSerializer('images', many=True)

  class Meta:
    model = Shoe
    fields = '__all__'
  
class BagSerializer(serializers.ModelSerializer):
  # images = PhotoInlineSerializer('images', many=True)

  class Meta:
    model = Bag
    fields = '__all__'
  
class ProductSerializer(serializers.ModelSerializer):
  class Meta:
    model = Product
    fields = '__all__'
