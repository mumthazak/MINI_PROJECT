from django.shortcuts import render
from user.models import User
from login.models import Login
# Create your views here.

def user(request):
    if request.method=='POST':
        obj=User()
        obj.name=request.POST.get('tname')
        obj.address= request.POST.get('aname')
        obj.phone=request.POST.get('phone')
        obj.email=request.POST.get('Email')
        obj.password=request.POST.get('pass')
        obj.save()

        ob = Login()
        ob.username = obj.name
        ob.password = obj.password
        ob.type = 'user'
        ob.uid=obj.r_id
        ob.save()
    return render(request,'user/register.html')

def manage(request):
    ii=request.session["u_id"]
    obj=User.objects.filter(r_id=ii)
    context = {
        'y': obj
    }
    return render(request,'user/mngprofile.html',context)


def update(request,idd):
    obj = User.objects.get(r_id=idd)
    context = {
        'objval': obj
    }
    if request.method=='POST':
        obj=User.objects.get(r_id=idd)
        obj.name=request.POST.get('tname')
        obj.address= request.POST.get('aname')
        obj.phone=request.POST.get('phone')
        obj.email=request.POST.get('Email')
        obj.password=request.POST.get('pass')
        obj.save()
    return render(request,'user/update.html',context)

def delete1(request,idd):
    ob=User.objects.get(r_id=idd)
    ob.delete()
    return manage(request)




