from django.conf.urls import url
from product import views
urlpatterns = [
    url('product/',views.prod),
    url('vprod/',views.vprod),
    url('crt/(?P<idd>\w+)',views.cart,name="cc")


]