from django.urls import path

from .views import *

urlpatterns = [
    path('shoes/get', ListShoes.as_view()),
    path(r'shoes/get/<int:id>', ListShoeById.as_view()),
    path('shoes/get/featured', ListFeaturedShoes.as_view()),
]
