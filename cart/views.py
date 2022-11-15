from django.shortcuts import render
from cart.models import Cart

# Create your views here

def vcart(request):
    ss=request.session["u_id"]
    obj=Cart.objects.filter(r_id=ss)
    context = {
        'x': obj
    }
    return render(request,'cart/vpp.html',context)