from django.urls import path,include
from django.contrib import admin
from.import views
urlpatterns=[
    path('cus_reg',views.cus_reg,name="cus_reg"),
    path('cuslogin',views.cuslogin,name="cuslogin"),
    path('cus_index',views.cus_index,name="cus_index"),
    path('shop<int:cid>',views.shop,name="shop"),
    path('view_all',views.view_all,name="view_all"),
    path('view_categ',views.view_categ,name="view_categ"),
    path('prod<int:pid>',views.prod,name="prod"),
    path('cart',views.cart,name="cart"),
    path('add_cart<int:pid>',views.add_cart,name="add_cart"),
    path('rem_cart<int:cid>',views.rem_cart,name="rem_cart"),
    path('increment_quantity<int:cart_id>',views.increment_quantity,name="increment_quantity"),
    path('decrement_quantity<int:cart_id>',views.decrement_quantity,name="decrement_quantity"),
    path('payment',views.payment,name="payment"),
    path('checkout',views.checkout,name="checkout"),

    path('order_complete',views.order_complete,name="order_complete"),
    path('add_wish<int:pid>',views.add_wish,name="add_wish"),
    path('view_wish',views.view_wish,name="view_wish"),

]