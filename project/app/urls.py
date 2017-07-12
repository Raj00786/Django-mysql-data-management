from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^$', views.nodeStatsView),
    url(r'^node/(?P<node_id>[\w-]+)/$',views.singleNodeView),
    url(r'^node/(?P<node_id>[\w-]+)/',views.filesDownload)
]
