from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from customer.models import *
from django.contrib import messages

# Create your views here.

def farm_reg(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        phno=request.POST['phone']
        pwd=request.POST['pass']
        add=request.POST['addr']
        repass=request.POST['repass']
        if pwd==repass:
            if Registeration.objects.filter(email=email).exists():
                messages.info(request,'email already exists')
            else:
                saveval=Registeration(name=name,email=email,phno=phno,password=pwd,address=add)
                saveval.save()
                return redirect('farmlogin')
        else:
            messages.info(request,'Password does not match') 
    return render(request,"farmer/farm_reg.html")

def farmlogin(request):
    if request.method=='POST':
        try:
            name=request.POST.get('name')
            pwd=request.POST.get('pass')
            check=Registeration.objects.get(name=name,password=pwd)
            request.session['id']=check.id
            request.session['name']=check.name
            return redirect('farm_index')
        except Registeration.DoesNotExist as e:
            messages.info(request,'invalid user')
    return render(request,"farmer/farm_login.html")
    #return render(request,'farmer/farm_login.html')

def farm_index(request):
    return render(request,"farmer/farm_index.html")                              

def add_prod(request):
    catall=Category.objects.all()
    if request.method=='POST':
        name=request.POST['name']
        pdes=request.POST['des']
        price=request.POST['price']
        stock=request.POST['stock']
        unit=request.POST['unit']
        categ=request.POST['categ']
        img=request.FILES.get('pimg')
        fid=request.session['id']
        catname=Product( pname=name,des=pdes,price=price,stock=stock,unit=unit,pimage=img,catid_id=categ,farmid_id=fid)
        catname.save()
        return redirect("add_prod")
    return render(request,"farmer/add_prod.html",{'catall':catall})

def add_cat(request):
   if request.method=='POST':
        name=request.POST['cat']
        img=request.FILES.get('cimg')
        fid=request.session['id']
        saveval=Category(cname=name,cimage=img,farmid_id=fid)
        saveval.save()
   return redirect('add_prod')  


def add_blog(request):
    if request.method=='POST':
        categ=request.POST['cat']
        bdes=request.POST['bdes']
        bimage=request.FILES.get('bimg')
        fid=request.session['id']
        saveval=Blog(categ=categ,bdes=bdes,bimage=bimage,farmid_id=fid)
        saveval.save()
        return redirect("add_blog")
    return render(request,"farmer/add_blog.html")

def view_cat(request):
    catall=Category.objects.all()
    return render(request,"farmer/view_cat.html",{'catall':catall})


def ed_cat(request,cid):
    upcat=Category.objects.get(id=cid)
    if request.method=='POST':
        upcat.cname=request.POST['cname']
        image_file=request.FILES.get('cimg')
        if image_file:
            upcat.cimage = image_file
            upcat.save()
        upcat.save()
        return redirect('view_cat')
    return render(request,'farmer/ed_cat.html',{'cat':upcat})  

def del_cat(request,cid):
    de_cat=Category.objects.get(id=cid)
    prod =Product.objects.filter(catid=cid)
    if request.method=="POST":
            if prod.count() < 1:
                de_cat.delete()
                return redirect("view_cat")
            else:
                messages.info(request,'This category contains atleast one product. Deletion Failed')

    return render(request,'farmer/del_cat.html',{'dcat':de_cat})

def view_prod(request):
    prod=Product.objects.all()
    print(prod.count())
    cat=Category.objects.all()
    context={
        'prod':prod,
        'cat':cat
        }
    return render(request,"farmer/view_prod.html",context)

def ed_prod(request,pid):
    catall=Category.objects.all()
    upprod=Product.objects.get(id=pid)
    context={
        'catall':catall,
        'prod':upprod
        }
    if request.method=='POST':
        upprod.pname=request.POST['pname']
        upprod.price=request.POST['price']
        upprod.stock=request.POST['stock']
        upprod.unit=request.POST['unit']
        upprod.des=request.POST['des']
        upprod.catid_id=request.POST['categ']
        
        image_file=request.FILES.get('pimg')
        if image_file:
            upprod.pimage = image_file
            upprod.save()
        upprod.save()
        return redirect('view_prod')
    return render(request,'farmer/ed_prod.html',context)
    #return render(request,'farmer/ed_prod.html')  

def del_prod(request,pid):
    de_prod=Product.objects.get(id=pid)
    if request.method=="POST":
        de_prod.delete()
        return redirect("view_prod")
    return render(request,'farmer/del_prod.html',{'dprod':de_prod})

def add_skill(request):
    if request.method=='POST':
        scat=request.POST['scat']
        sdes=request.POST['sdes']
        simage=request.FILES.get('simg')
        fid=request.session['id']
        saveval=Skill(scat=scat,sdes=sdes,simage=simage,farmid_id=fid)
        saveval.save()
        return redirect("add_skill")
    return render(request,"farmer/add_skill.html")

def skill_blog(request):
    skl=Skill.objects.all()
    blg=Blog.objects.all()
    context={
        'skl':skl,
        'blg':blg
        }
    return render(request,"farmer/skill_blog.html",context)

def ed_skill(request,sid):
    upskill=Skill.objects.get(id=sid)
    if request.method=='POST':
        upskill.scat=request.POST['scat']
        upskill.sdes=request.POST['sdes']
        image_file=request.FILES.get('simg')
        if image_file:
            upskill.simage = image_file
            upskill.save()
        upskill.save()
        return redirect('skill_blog')
    return render(request,'farmer/ed_skill.html',{'skl':upskill})  

def ed_blog(request,bid):
    upblog=Blog.objects.get(id=bid)
    if request.method=='POST':
        upblog.categ=request.POST['bcat']
        upblog.bdes=request.POST['bdes']
        image_file=request.FILES.get('bimg')
        if image_file:
            upblog.bimage = image_file
            upblog.save()
        upblog.save()
        return redirect('skill_blog')
    return render(request,'farmer/ed_blog.html',{'blg':upblog})  

def del_skill(request,sid):
    de_skill=Skill.objects.get(id=sid)
    if request.method=="POST":
        de_skill.delete()
        return redirect("skill_blog")
    return render(request,'farmer/del_skill.html',{'dskill':de_skill})

def del_blog(request,bid):
    de_blog=Blog.objects.get(id=bid)
    if request.method=="POST":
        de_blog.delete()
        return redirect("skill_blog")
    return render(request,'farmer/del_blog.html',{'dblog':de_blog})

def order_details(request):
    orders =Cart.objects.filter(farmid=request.session['id'])
    return render(request,'farmer/orders.html',{"orders":orders})

