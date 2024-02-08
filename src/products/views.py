from rest_framework.views import APIView
from rest_framework import authentication, permissions, status
from rest_framework.response import Response

from .models import *
from .serializers import *

# Shoes
class ListShoes(APIView):
  def get(self, request):
    shoes = Shoe.objects.all()
    shoe_serializer = ShoeSerializer(shoes, many=True)

    return Response({"shoes": shoe_serializer.data}, status.HTTP_200_OK)


class ListShoeById(APIView):
  def get(self, request, **kwargs):
    shoe = Shoe.objects.filter(id=self.kwargs["id"]).first()
    shoe_serializer = ShoeSerializer(shoe)
    
    return Response({"shoe": shoe_serializer.data}, status.HTTP_200_OK)


class ListFeaturedShoes(APIView):
  def get(self, request):
    shoes = Shoe.objects.filter(featured=True)
    shoe_serializer = ShoeSerializer(shoes, many=True)

    return Response({"shoes": shoe_serializer.data}, status.HTTP_200_OK)


# Products
# TODO See if we can get model type from Product
class ListAllProducts(APIView):
  def get(self, request):
    shoes = Shoe.objects.all()
    shoe_serializer = ShoeSerializer(shoes, many=True)

    bag = Bag.objects.all()
    bag_serializer = BagSerializer(bag, many=True)

    data = shoe_serializer.data + bag_serializer.data

    return Response({"shoes": shoe_serializer.data, "bags": bag_serializer.data}, status.HTTP_200_OK)

# TODO Get product by id and get all the data based on 
# TODO Model type.
class GetProductById(APIView):
  def get(self, request):
    shoes = Shoe.objects.all()
    shoe_serializer = ShoeSerializer(shoes, many=True)

    bag = Bag.objects.all()
    bag_serializer = BagSerializer(bag, many=True)

    data = shoe_serializer.data + bag_serializer.data

    return Response({"shoes": shoe_serializer.data, "bags": bag_serializer.data}, status.HTTP_200_OK)