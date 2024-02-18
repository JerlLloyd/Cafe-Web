from django.urls import path

from myapp.controller import authview, cart, wishlist, checkout

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("collections", views.collections, name="collections"),
    path("collections/<str:sid>", views.collectionsview, name="collectionsview"),
    path("collections/<str:fat_sid>/<str:prod_sid>", views.productview, name='productview'),
    
    path("register/", authview.register, name="register"),
    path("login/", authview.loginpage, name="loginpage"),
    path("logout/", authview.logoutpage, name="logout"),
    path("to-cart", cart.addtocart, name="addtocart"),
    path("cart/", cart.viewcart, name="cart"),
    path("update-cart", cart.updatecar, name="updatecar"),
    path("delete-cart-item", cart.deletecartitem, name="deletecartitem"),
    path("wishlist", wishlist.wish_list , name="wishlist"),
    path("add-to-wishlist", wishlist.addtowish,  name="addtowish"),
    path('delete-wishlist-item', wishlist.deleteitem, name="deletewishlistitm"),
    
    path('checkout', checkout.checks  , name="checkout"),
    path('placeorder', checkout.placeorder  , name="placeorder"),
]
