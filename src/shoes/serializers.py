from rest_framework import serializers
from .models import Shoe

class ShoeSerializer(serializers.ModelSerializer):
  class Meta:
    model = Shoe
    depth = 1
    fields = '__all__'