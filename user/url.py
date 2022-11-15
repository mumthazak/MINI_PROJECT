from django.conf.urls import url
from user import views

urlpatterns = [
    url('user',views.user),
    url('mng/',views.manage),
    url('updt/(?P<idd>\w+)',views.update,name="up"),
    url('dlt/(?P<idd>\w+)', views.delete1,name="dl1")


]