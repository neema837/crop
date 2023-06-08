from django.urls import path,include
from django.contrib import admin
from.import views

urlpatterns=[

    path('brinjalpred',views.brinjalpred,name="brinjalpred"),
    path('brinjalprediction',views.brinjalprediction,name="brinjalprediction"),
    path('welcomepred',views.welcomepred,name="welcomepred"),
]