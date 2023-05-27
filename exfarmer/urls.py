from django.urls import path,include
from django.contrib import admin
from.import views
urlpatterns=[
    path('exfarm_reg',views.exfarm_reg,name="exfarm_reg"),
    path('exfarmlogin',views.exfarmlogin,name="exfarmlogin"),
    path('exfarm_index',views.exfarm_index,name="exfarm_index"),
]