from django.shortcuts import render
from product.models import Product
from django.core.files.storage import FileSystemStorage
from cart.models import Cart
# Create your views here.

def prod(request):
    if request.method == 'POST':
        obj=Product()
        obj.p_name=request.POST.get('Product')
        myfile=request.FILES['img']
        fs=FileSystemStorage()
        filename=fs.save(myfile.name,myfile)
        obj.image =myfile.name
        obj.description = request.POST.get('dis')
        obj.amount= request.POST.get('amt')
        obj.save()
    return render(request, 'product/product.html')

def vprod(request):
    obj=Product.objects.all()
    context = {
        'x': obj
    }
    return render(request,'product/viewproduct.html',context)
def cart (request,idd):
    ss=request.session["u_id"]
    ob=Cart()
    ob.p_id=idd
    ob.r_id=ss
    ob.save()
    return vprod(request)



