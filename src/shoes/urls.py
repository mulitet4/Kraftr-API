from django.urls import path

from .views import ListShoes

urlpatterns = [
    path('get', ListShoes.as_view()),
]
