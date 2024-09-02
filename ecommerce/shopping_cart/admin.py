from django.contrib import admin
from .models import *
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("product_name",)}
    
admin.site.register(Customer)
admin.site.register(CustomerCart)
admin.site.register(ShippingAddress)
admin.site.register(OrderItem)
admin.site.register(Product, ProductAdmin)