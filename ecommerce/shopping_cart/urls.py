from django.urls import path
from . import views

urlpatterns = [
    path('', views.AllProducts),
    path('cart/', views.Cart, name="cart")
]
