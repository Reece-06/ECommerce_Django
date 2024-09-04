from django.contrib import admin
from .models import *
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("product_name",)}
    list_display = ["product_name", "price", "quantity"]

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ["product", "item_quantity", "date_ordered"]
    list_filter = ("cart", "date_ordered",)

admin.site.register(Customer)
admin.site.register(CustomerCart)
admin.site.register(ShippingAddress)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Product, ProductAdmin)