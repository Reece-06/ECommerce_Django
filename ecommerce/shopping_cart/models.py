from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
class ShippingAddress(models.Model):
    #address_id = models.SmallAutoField()
    address = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    zip = models.IntegerField(validators=[
        MaxValueValidator(99999), 
        MinValueValidator(100)
        ])
    
    class Meta:
        verbose_name_plural = "Shipping addresses"

    def __str__(self):
        return self.address
    
    
    
class Customer(models.Model):
    #user_id = models.SmallAutoField()
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=30)
    address = models.OneToOneField(ShippingAddress, on_delete=models.SET_NULL, null=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    
    def getfullname(self):
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self):
        return self.getfullname()

class Product(models.Model):
    #product_id = models.SmallAutoField()
    product_name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    quantity = models.IntegerField()
    image = models.CharField(max_length=30)
    slug = models.SlugField(max_length=50, default="", blank=True)

    class Meta:
        indexes = [
            models.Index(fields=["slug"])
        ]

    def __str__(self):
        return self.product_name

class CustomerCart(models.Model):
    #cart_id = models.SmallAutoField()
    user = models.OneToOneField(Customer, on_delete=models.CASCADE)
    

    def __str__(self):
        return f"Cart of {self.user.getfullname()}"

class OrderItem(models.Model):
    #order_id = models.SmallAutoField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date_ordered = models.DateField(auto_now=True, editable=True)
    item_quantity = models.IntegerField() 
    cart = models.ForeignKey(CustomerCart, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return f"{self.product.product_name} (Qty: {self.item_quantity})"




