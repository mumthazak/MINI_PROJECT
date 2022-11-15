from django.shortcuts import render
from product.models import Product
from order.models import Orders
from cart.models import Cart
from user.models import User
import datetime


# Create your views here.

# def ord(request):
    # ob=Register.objects.all()
    # context={
    #     'objval':ob
    # }
    # if request.method=='POST':
    #     obj=Orders()
    #     obj.r_id=request.POST.get('uu')
    #     obj.p_id =1
    #     obj.quantity = request.POST.get('quan')
    #     obj.date=datetime.datetime.today()
    #     obj.time=datetime.datetime.now()
    #     obj.save()
    # return render(request,'order/order.html',context)


def vord(request):
    ss = request.session["u_id"]
    obj=Cart.objects.filter(r_id=ss)
    context = {
        'x': obj
    }
    return render(request,'order/ord.html',context)
def order(request,idd):
    ss=request.session["u_id"]
    if request.method=='POST':
        ob=Orders()
        ob.r_id=ss
        ob.p_id=idd
        ob.quantity=request.POST.get('quan')
        ob.date=request.POST.get('date')
        ob.time=request.POST.get('time')
        ob.location=request.POST.get('loc')
        ob.save()
    return render(request,'order/order.html')

def vieword(request):
    ss = request.session["u_id"]
    obj=Orders.objects.all()
    context = {
        'x': obj
    }
    return render(request,'order/vieworder.html',context)


def myord(request):
    ss=request.session["u_id"]
    obj=Orders.objects.filter(r_id=ss)
    context = {
        'objval': obj
    }
    return render(request,'order/my order.html',context)


def remove(request,idd):
    ob=Cart.objects.get(p_id=idd).delete()
    return vord(request)


