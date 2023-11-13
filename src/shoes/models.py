from django.db import models

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
  

class Shoe(models.Model):
  # Images
  # Stock
  name = models.CharField(max_length=100)
  shoe_type = models.ForeignKey(ShoeType, models.SET_NULL, null=True)
  shoe_sizes = models.ManyToManyField(ShoeSize)

  def __str__(self) -> str:
    return self.name + " " + str(self.shoe_type)