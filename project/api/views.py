from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, ListCreateAPIView
from rest_framework import permissions
from app.models import NodeStats,NodeData
from .serializers import NodeStatsSerializers,NodeDataSerializers
from django.core.urlresolvers import resolve
from django.contrib.auth.models import User


class NodeListAPIView(ListCreateAPIView):
	queryset = NodeStats.objects.all()
	serializer_class = NodeStatsSerializers
	lookup_field= 'node_id'
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class NodeDetailAPIView(ListAPIView):
	serializer_class = NodeDataSerializers
	lookup_field= 'node'
	lookup_url_kwarg = 'nodeid'
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
	
	def get_queryset(self):
		name = self.kwargs.get(self.lookup_url_kwarg)
		data = NodeData.objects.filter(node_id=name).order_by('-pk')
		return data

class NodeUpdateAPIView(UpdateAPIView):
	queryset = NodeData.objects.all()
	serializer_class = NodeDataSerializers
	lookup_field= 'node'
	lookup_url_kwarg = 'nodeid'
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class NodeDestroyAPIView(DestroyAPIView):
	queryset = NodeData.objects.all()
	serializer_class = NodeDataSerializers
	lookup_field= 'node'
	lookup_url_kwarg = 'nodeid'	
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

