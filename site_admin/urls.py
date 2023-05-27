from django.urls import path,include
from django.contrib import admin
from.import views
urlpatterns=[
    path('admin_index',views.admin_index,name="admin_index"),
    path('admin_login',views.admin_login,name="admin_login"),
    path('appr_exfarm',views.appr_exfarm,name="appr_exfarm"),
    path('e_approve<int:eid>',views.e_approve,name="e_approve"),
    path('e_reject<int:eid>',views.e_reject,name="e_reject"),
    path('send_email<int:id>',views.send_email,name="send_email"),
    path('send_remail<int:id>',views.send_remail,name="send_remail"),
]