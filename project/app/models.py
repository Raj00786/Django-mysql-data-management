from __future__ import unicode_literals

from django.db import models

class NodeStats(models.Model):
	node_id 	= models.IntegerField(primary_key=True, unique=True,blank=False)
	name 		= models.CharField(max_length=120)
	location 	= models.CharField(max_length=120)
	timestamp 	= models.DateTimeField(auto_now=False,auto_now_add=True)

	def __str__(self):
		return "node : "+self.name

class NodeData(models.Model):
	node 		= models.ForeignKey(NodeStats,on_delete=models.CASCADE,default=1)
	battery_str = models.CharField(max_length=120)
	signal_str 	= models.CharField(max_length=120,default='100')
	timestamp 	= models.DateTimeField(auto_now=False,auto_now_add=True)
	data 		= models.TextField()

	def __str__(self):
		return  str(self.node)
