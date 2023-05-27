from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib import messages

# Create your views here.
def exfarm_reg(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        phno=request.POST['phone']
        #pwd=request.POST['pass']
        add=request.POST['addr']
        #repass=request.POST['repass']
        
        saveval=ExpFarmer(name=name,email=email,phno=phno,address=add)
        saveval.save()
        return redirect('exfarmlogin')
       
    return render(request,"exfarmer/exfarm_reg.html")

def exfarmlogin(request):
    if request.method=='POST':
        try:
            name=request.POST.get('name')
            pwd=request.POST.get('pass')
            check=ExpFarmer.objects.get(name=name,password=pwd)
            request.session['id']=check.id
            request.session['name']=check.name
            return redirect('exfarm_index')
        except ExpFarmer.DoesNotExist as e:
            messages.info(request,'invalid user')
    return render(request,"exfarmer/exfarm_login.html")
    #return render(request,'farmer/farm_login.html')

def exfarm_index(request):
    return render(request,"exfarmer/exfarm_index.html") 