from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from polymorphic.models import PolymorphicModel

# Generic Models
class Photo(models.Model):
  image = models.ImageField(upload_to='images/products')
  name = models.CharField(max_length=100)

class Product(PolymorphicModel):
  name = models.CharField(max_length=100)
  price = models.IntegerField()
  featured = models.BooleanField(default=False)
  description = models.TextField()
  

# Shoe Models
class ShoeType(models.Model):
  name = models.CharField(max_length=100)

  def __str__(self) -> str:
    return self.name

class ShoeSize(models.Model):
  class ShoeSizeType(models.TextChoices):
    US = 'US', 'US Shoe Size Measuring System'
    EU = 'EU', 'EU Shoe Size Measuring System'
    EK = 'UK', 'UK Shoe Size Measuring System'
  
  shoe_size_type = models.CharField(
    max_length=20,
    choices=ShoeSizeType.choices,
    default=ShoeSizeType.US
  )
  size = models.IntegerField()
  
  def __str__(self):
      return self.shoe_size_type + " " + str(self.size)

class Shoe(Product):
  stock = models.IntegerField(default=0)
  cover_image = models.ImageField(null=True, blank=True, upload_to='images/products')
  images = models.ManyToManyField(Photo, blank=True)
  shoe_type = models.ForeignKey(ShoeType, models.SET_NULL, null=True)
  shoe_sizes = models.ManyToManyField(ShoeSize)

  def __str__(self) -> str:
    return self.name + " " + str(self.shoe_type)


# Bag Models
# TODO Make size a model itself.
class Bag(Product):
  size = models.IntegerField(default=0)

  def __str__(self):
      return self.name