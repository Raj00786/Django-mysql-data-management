from django.conf.urls import url
from django.contrib import admin
from .views import NodeListAPIView,NodeDetailAPIView,NodeUpdateAPIView,NodeDestroyAPIView

urlpatterns = [
    url(r'^$',NodeListAPIView.as_view(),name='Node_list'),

    url(r'^(?P<nodeid>[\w-]+)/$',NodeDetailAPIView.as_view(),name='detail'),
    url(r'^(?P<nodeid>[\w-]+)/update/$',NodeUpdateAPIView.as_view(),name='update'),
    url(r'^(?P<nodeid>[\w-]+)/delete/$',NodeDestroyAPIView.as_view(),name='delete'),
    url(r'^(?P<nodeid>[\w-]+)/$',NodeDestroyAPIView.as_view(),name='delete'),

]