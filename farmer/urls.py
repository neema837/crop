from django.urls import path,include
from django.contrib import admin
from.import views
urlpatterns=[
    path('farm_reg',views.farm_reg,name="farm_reg"),
    path('farmlogin',views.farmlogin,name="farmlogin"),    
    path('farm_index',views.farm_index,name="farm_index"),
    path('add_prod',views.add_prod,name="add_prod"),
    path('add_cat',views.add_cat,name="add_cat"),
    path('add_blog',views.add_blog,name="add_blog"),
    path('view_cat',views.view_cat,name="view_cat"),
    path('ed_cat<int:cid>',views.ed_cat,name="ed_cat"),
    path('view_prod',views.view_prod,name="view_prod"),
    path('del_cat<int:cid>',views.del_cat,name="del_cat"),
    path('ed_prod<int:pid>',views.ed_prod,name="ed_prod"),
    path('del_prod<int:pid>',views.del_prod,name="del_prod"),
    path('add_skill',views.add_skill,name="add_skill"),
    path('skill_blog',views.skill_blog,name="skill_blog"),
    path('ed_skill<int:sid>',views.ed_skill,name="ed_skill"),
    path('ed_blog<int:bid>',views.ed_blog,name="ed_blog"),
    path('del_skill<int:sid>',views.del_skill,name="del_skill"),
    path('del_blog<int:bid>',views.del_blog,name="del_blog"),

    path('order_details',views.order_details,name="order_details"),

    
]