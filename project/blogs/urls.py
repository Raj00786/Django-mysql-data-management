from django.conf.urls import url,include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$',views.post_home,name="home"),
    url(r'^create/$',views.post_create,name="create"),
    url(r'^(?P<slug>[\w-]+)/$',views.details,name="detail"),
    url(r'^(?P<slug>[\w-]+)/edit/$',views.post_update,name="update"),
    url(r'^(?P<slug>[\w-]+)/delete/$',views.post_delete,name="delete"),
]
