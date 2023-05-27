from django.urls import path,include
from django.contrib import admin
from.import views
urlpatterns=[
    path('',views.index,name="index"),
    path('login',views.login,name="login"),   
    path('exfarm_login',views.exfarm_login,name="exfarm_login"),
    path('cus_login',views.cus_login,name="cus_login"),
    
    path('exfarm_reg',views.exfarm_reg,name="exfarm_reg"),
    path('cus_reg',views.cus_reg,name="cus_reg"),
]