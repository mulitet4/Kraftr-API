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

class ListShoeById(APIView):
  def get(self, request, **kwargs):
    print(self.kwargs)
    shoe = Shoe.objects.filter(id=self.kwargs["id"]).first()
    shoe_serializer = ShoeSerializer(shoe)
    return Response({"shoe": shoe_serializer.data}, status.HTTP_200_OK)
  
class ListFeaturedShoes(APIView):
  def get(self, request):
    shoes = Shoe.objects.filter(featured=True)
    shoe_serializer = ShoeSerializer(shoes, many=True)

    return Response({"shoes": shoe_serializer.data}, status.HTTP_200_OK)