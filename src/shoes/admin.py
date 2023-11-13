from django.contrib import admin
from .models import Shoe, ShoeSize, ShoeType

# Register your models here.
admin.site.register(Shoe)
admin.site.register(ShoeSize)
admin.site.register(ShoeType)