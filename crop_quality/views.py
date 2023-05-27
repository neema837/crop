from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,"index.html")



def exfarm_reg(request):
    return render(request,"exfarm_reg.html")

def cus_reg(request):
    return render(request,"cus_reg.html")

def login(request):
    return render(request,"login.html")

def exfarm_login(request):
    return render(request,"exfarm_login.html")

def cus_login(request):
    return render(request,"cus_login.html")
    