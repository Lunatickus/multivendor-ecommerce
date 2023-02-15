from django.contrib import admin
from .models import *

admin.site.register(Vendor)
admin.site.register(ProductCategory)
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItems)
admin.site.register(CustomerAddress)
admin.site.register(ProductRating)
