from django.shortcuts import render
from feedback.models import Feedback
import datetime
# Create your views here.
def feed(request):
    if request.method=='POST':
        obj=Feedback()
        obj.feedback=request.POST.get('fname')
        obj.r_id='1'
        obj.date=datetime.datetime.now()
        obj.save()
    return render(request,'feedback/post_feedback.html')


def vfeed(request):
    obj=Feedback.objects.all()
    context={
        'x':obj,
    }
    return render(request,'feedback/view_feedback.html',context)

