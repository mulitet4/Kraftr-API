from rest_framework import serializers
from .models import Shoe, ShoeSize, ShoeType, Photo

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
    fields = ['id', 'name', 'shoe_type', 'shoe_sizes', 'stock', 'cover_image', 'images', 'featured', 'price', 'description']