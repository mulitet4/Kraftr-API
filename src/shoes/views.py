from rest_framework.views import APIView
from rest_framework import authentication, permissions, status
from rest_framework.response import Response

from .models import Shoe
from .serializers import ShoeSerializer

class ListShoes(APIView):
  def get(self, request):
    shoes = Shoe.objects.all()
    shoe_serializer = ShoeSerializer(shoes, many=True)

    return Response({"shoes": shoe_serializer.data}, status.HTTP_200_OK)