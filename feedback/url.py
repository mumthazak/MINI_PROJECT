from django.conf.urls import url
from feedback import views

urlpatterns=[
    url('pfeedback/',views.feed),
    url('vfeedback',views.vfeed)
]