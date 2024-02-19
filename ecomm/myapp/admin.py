from django.contrib import admin

from .models import *

admin.site.register(Category)
admin.site.register(product)
admin.site.register(Cart)
admin.site.register(Wishlist)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Profile)

# Register your models here.
