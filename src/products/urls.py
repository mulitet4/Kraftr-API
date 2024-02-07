from django.urls import path

from .views import *

urlpatterns = [
    path('shoes/get', ListShoes.as_view()),
    path(r'shoes/get/<int:id>', ListShoeById.as_view()),
    path('shoes/get/featured', ListFeaturedShoes.as_view()),
    path('get', ListAllProducts.as_view()),
    path('get/<int:id>', GetProductById.as_view()),
]
