from django.db import models
from src.products.models import Product
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager

# TODO Create a custom User Model with the fields for 
# TODO Address, Pincode, Payment stuff, etc.
# TODO https://testdriven.io/blog/django-custom-user-model/

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    address1 = models.TextField(default="")
    address2 = models.TextField(default="")
    address3 = models.TextField(default="")
    pincode = models.IntegerField(default=0)
    first_name = models.CharField(default="")
    last_name = models.CharField(default="")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Cart(models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE)
  cart = models.ManyToManyField(Product)

