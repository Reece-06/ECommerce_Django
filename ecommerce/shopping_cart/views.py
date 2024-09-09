from django.shortcuts import render
from .models import *
# Create your views here.
def SegregateOrderedItems(ordered_items):
    all_products = Product.objects.all() 
    segregated_items = []
    for product in all_products:
        product_image = product.image
        product_name = product.product_name
        product_price = product.price
        product_total = 0 
        product_qty = 0
        isfirst = True
        new_item = {}
        
        for item in ordered_items:
            if product.id == item.product.id:
                if isfirst: 
                    new_item = {
                        "item_image": product_image, 
                        "item_name": product_name, 
                        "item_price": product_price, 
                        "item_total": product_total, 
                        "item_qty": product_qty
                    }
                    isfirst = False

                new_item["item_qty"]+=item.item_quantity
                new_item["item_total"]+=new_item["item_price"]*item.item_quantity

        if new_item != {}:
            segregated_items.append(new_item)
    return segregated_items

def GetOrderedItemCount(items):
    count = 0
    for item in items: 
        count+=item["item_qty"]

    return count

def GetTotalOfAllItems(items):
    overall_total = 0
    for item in items:
        overall_total+=item["item_total"]

    return overall_total
        

def GetOrderedItems():
    user_reece = Customer.objects.get(id=2) # id is currrently a static value.
    #reece_id = user_reece.id
    
    reece_cart = CustomerCart.objects.get(user=user_reece)
 
    all_ordered_items = OrderItem.objects.filter(cart=reece_cart).order_by("product__product_name")
    print(f"all_ordered_items: {all_ordered_items}")
    return all_ordered_items

def AllProducts(request):
    all_products = Product.objects.all()
    return render(request, "shopping_cart/all-products.html", {
        "products": all_products,
    })

def Cart(request):
    all_ordered_items = GetOrderedItems()
    segregated_items = SegregateOrderedItems(all_ordered_items)
    items_count = GetOrderedItemCount(segregated_items)  
    items_total = GetTotalOfAllItems(segregated_items)
    items_len = len(all_ordered_items)
    return render(request, "shopping_cart/cart.html", {
        "segregated_items": segregated_items, 
        "items_count": items_count,
        "items_total": items_total,
    })