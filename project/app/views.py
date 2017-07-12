from django.shortcuts import render,HttpResponse
from .models import NodeStats,NodeData
import csv

# Create your views here.

def nodeStatsView(request):
	data = NodeStats.objects.all()
	return render(request,'index.html',{'data':data})

def singleNodeView(request,node_id):
	node = NodeData.objects.filter(node_id=node_id).order_by('-timestamp')
	return render(request,'single.html',{'data':node,'nodeid':node_id})

def filesDownload(request,node_id):
	data = NodeData.objects.filter(node_id=node_id).order_by('-timestamp')
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename="node_'+node_id+'.csv"'
	writer = csv.writer(response)
	writer.writerow(['datetime','battery_str','signal_str','data'])
	for d in data:
		print(d.node_id)
		writer.writerow([d.timestamp,d.battery_str,d.signal_str,d.data])
	return response;