from django.urls import path

from .views import *

urlpatterns = [
    path("register", register),
    path("login", login),
    path("cart", ListCart.as_view()),
    path("cart/add", addCart),
]
