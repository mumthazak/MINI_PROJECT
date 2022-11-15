from django.conf.urls import url
from order import views
urlpatterns = [
    # url('order/',views.ord),
    url('vord/',views.vord),
    url('rmv/(?P<idd>\w+)',views.remove,name="rm"),
    url('post/(?P<idd>\w+)',views.order,name="ord"),
    url('view/',views.vieword),
    url('viewmyorder/',views.myord)


]