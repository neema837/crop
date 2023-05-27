from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import *
from farmer.models import *
from django.contrib import messages
from crop_assessment.settings import RAZORPAY_API_KEY,RAZORPAY_API_SECRET_KEY
import razorpay
from datetime import date

# Create your views here.

def cus_reg(request):
    if request.method=='POST':
        name=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        phno=request.POST['phone']
        pwd=request.POST['pass']
        local=request.POST['local']
        adtype=request.POST['adtype']
        zipcode=request.POST['zipcode']
        state=request.POST['adstate']
        add=request.POST['addr']
        repass=request.POST['repass']
        if pwd==repass:
            if customer.objects.filter(email=email).exists():
                messages.info(request,'email already exists')
            else:
                saveval=customer(name=name,lname=lname,email=email,phno=phno,password=pwd,address=add,locality=local,adtype=adtype,zipcode=zipcode,state=state)
                saveval.save()
                return redirect('cuslogin')
        else:
            messages.info(request,'Password does not match') 
    return render(request,"customer/cus_reg.html")

def cuslogin(request):
    if request.method=='POST':
        try:
            name=request.POST.get('name')
            pwd=request.POST.get('pass')
            check=customer.objects.get(name=name,password=pwd)
            request.session['id']=check.id
            request.session['name']=check.name
            return redirect('cus_index')
        except customer.DoesNotExist as e:
            messages.info(request,'invalid user')
    return render(request,"customer/cus_login.html")
    #return render(request,'farmer/farm_login.html')

def cus_index(request):
    cat=Category.objects.all()
    return render(request,"customer/cus_index.html",{'cat':cat}) 

def shop(request,cid):
    cat=Category.objects.get(id=cid)
    prod=Product.objects.filter(catid=cid)
    return render(request,"customer/shop.html",{'prod':prod}) 

def view_categ(request):
    catall=Category.objects.all()
    return render(request,"customer/view_categ.html",{'catall':catall}) 

def view_all(request):
    prod=Product.objects.all()
    return render(request,"customer/shop.html",{'prod':prod}) 

def rem_cart(request,cid):
    cart = get_object_or_404(Cart, pk=cid)
    cart.delete()
    return redirect('cart')

def prod(request,pid):
    prod=Product.objects.get(id=pid)
    cus_id=request.session['id']
    wish=wishlist.objects.filter(cusid=cus_id,pid=pid)
    items=wish.count()
    context={
        'prod':prod,
        'items':items
    }
    return render(request,"customer/prod.html",context)

def cart(request):
    today=date.today()
    cus_id=request.session['id']
    item=Cart.objects.filter(cusid=cus_id,created_at=today,paystatus=False)
    print(item.count())
    count_val=item.count()
    sub_tot =  0
    tot = 0
    total = 0
    for i in item:
        sub_tot = i.pid.price * i.qty
        tot = tot + sub_tot
        Cart.objects.filter(id=i.id).update(subtotal=sub_tot)
    total = tot
    context={
        'item':item,
        'total':total,
        'count_val':count_val
        }
    return render(request,"customer/cart.html",context)
global cart_id  
cart_id =   0
def add_cart(request,pid):
    if request.method=="POST":
        cuid=request.session['id']
        proid=pid
        qty=request.POST['qty']
        prod=Product.objects.get(id=pid)
        price=prod.price
        if Cart.objects.filter(cusid=cuid,pid=proid,paystatus=False).exists():
            cart = Cart.objects.filter(pid=pid,paystatus=False)
            for c in cart:
                print(c.id)
                global cart_id
                cart_id = c.id
            cart = get_object_or_404(Cart, pk=cart_id)
            cart.qty += 1
            cart.save()
            sub_tot = cart.pid.price * cart.qty
            Cart.objects.filter(id=cart_id).update(subtotal=sub_tot)
            return redirect('cart')
        else:
            saveval=Cart(cusid_id=cuid,pid_id=proid,qty=qty,subtotal=price)
            saveval.save()
            return redirect('cart')

    item=Cart.objects.filter(paystatus=False,cusid=cuid)
    return render(request,"customer/cart.html",{'item':item})

def increment_quantity(request, cart_id):
    if request.method=="POST":
        cart = get_object_or_404(Cart, pk=cart_id)
        cart.qty += 1
        cart.save()
    return redirect('cart')

def decrement_quantity(request, cart_id):
    if request.method=="POST":
        cart = get_object_or_404(Cart, pk=cart_id)
        if cart.qty == 1:
            cart.delete()
        else:
            cart.qty -= 1
            cart.save()
    return redirect('cart')

def checkout(request):
    cus_details=customer.objects.get(id=request.session['id'])
    cart_items=Cart.objects.filter(cusid=request.session['id'],paystatus=False)
    if request.method=="POST":
        cusid=request.session['id']
        email=request.POST['email']
        phno=request.POST['phone']
        local=request.POST['local']
        adtype=request.POST['adtype']
        zipcode=request.POST['zipcode']
        state=request.POST['adstate']
        add=request.POST['addr']       
        cid = []
        for i in cart_items:
            cid.append(i.id)
    
        order_VALUE=Orders.objects.create(cusid_id=cusid,email=email,phno=phno,locality=local,adtype=adtype,zipcode=zipcode,state=state,address=add)
        for c in cid:
            order_VALUE.cartid.add(Cart.objects.get(id=c))

    context={
                'cus_details':cus_details,
                'cart_items':cart_items,
        }

    return render(request,"customer/checkout.html",context)

def payment(request):
    today=date.today()
    cus_id=request.session['id']
    item=Cart.objects.filter(cusid=cus_id,created_at=today,paystatus=False)
    sub_tot =  0
    tot = 0
    total = 0
    for i in item:
        sub_tot = i.pid.price * i.qty
        tot = tot + sub_tot
    total = tot
    cus_details=customer.objects.get(id=cus_id)

    #for i in item:
        #cartid=
    #cart = Cart.objects.get(cusid=request.session['id'])
    
        #order.cartid.set(cart.cartid.all())
    
    currency ="INR"
    api_key=RAZORPAY_API_KEY
    amt=int(total)*100  
    payment_order= client.order.create(dict(amount=amt,currency="INR",payment_capture=1))
    payment_order_id= payment_order['id']
    context={
        'item':item,
        'total':total,
        'cus_details':cus_details,
        'api_key':api_key,
        'order_id':payment_order_id
        }
    
   
    return render(request,"customer/payment.html",context)

client = razorpay.Client(auth=(RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY))


def order_complete(request):
    today=date.today()
    Cart.objects.filter(cusid=request.session['id'],created_at=today).update(paystatus=True)
    for i in  Cart.objects.filter(cusid=request.session['id'],created_at=today):
        print (i.cusid,i.created_at)
    return render(request,"customer/order_complete.html")

def add_wish(request,pid):
    prod=Product.objects.get(id=pid)
    cus_id=request.session['id']
    prod_id=pid
    farmid=prod.farmid
    saveval=wishlist(cusid_id=cus_id,pid_id=prod_id,farmid=farmid)
    saveval.save()
    wish=wishlist.objects.filter(cusid=cus_id,pid=pid)
    items=wish.count()
    context={
        'prod':prod,
        'items':items
    }
    return render(request,"customer/prod.html",context)

def view_wish(request):
    cus_id=request.session['id']
    wish=wishlist.objects.filter(cusid=cus_id)
    return render(request,"customer/wishlist.html",{'wish':wish})