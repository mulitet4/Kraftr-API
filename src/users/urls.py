from django.urls import path

from .views import *

urlpatterns = [
    path("register", register),
    path("login", login),
    path("cart", ListCart.as_view()),
    path("cart/quantity/change", changeCartQuantity),
    path("cart/add", addCart),
    path("cart/delete/<int:id>", deleteCart),
]
