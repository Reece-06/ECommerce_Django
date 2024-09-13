from django.urls import path
from . import views

urlpatterns = [
    path('', views.AllProducts, name="all-products"),
    path('cart/', views.Cart, name="cart"),
    path('update_item/', views.updateItem),
]
