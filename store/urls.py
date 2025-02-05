from multiprocessing.resource_tracker import register
from tkinter.font import names

from django.urls import path,include
from . import views
from .views import collections
from store.controller import authview, cart, wishlist, checkout, order
urlpatterns = [

    path('home/', views.home, name='home'),
    path('', views.home, name='home'),
    path('collections', views.collections, name='collections'),
    path('collections/<str:slug>', views.collectionsview, name='collectionsview'),
    path('collections/<str:cate_slug>/<str:prod_slug>', views.productview, name='productview'),

   path('product-list', views.productlistAjax),
    path('searchproduct', views.searchproducts, name='searchproduct'),
    path('register/', authview.register, name='register'),# Add this line for the root URL
    path('login/', authview.loginpage, name='loginpage'),
    path('logout/', authview.logoutpage, name='logoutpage'),
    path('add-to-cart', cart.addtocart, name='addtocart'),
    path('cart',cart.viewcart, name="cart"),
    path('update-cart', cart.updatecart, name="updatecart"),
    path('delete-cart-item', cart.deletecartitem, name="deletecartitem"),
    path('wishlist', wishlist.index, name='wishlist'),
    path('add-to-wishlist',wishlist.addtowishlist, name="addtowishlist"),
    path('delete-wishlist-item', wishlist.deletewishlistitem, name="deletewishlistitem"),
    path('checkout', checkout.index, name='checkout'),
    path('placeorder', checkout.placeorder, name='placeorder'),
    path('my-orders',order.index, name='myorders'),
    path('view-order/<str:t_no>',order.vieworder, name='orderview'),



]
