from django.contrib import admin
from .models import NodeStats,NodeData
# Register your models here.
class NodeModelAdmin(admin.ModelAdmin):
	list_display = ['node_id','timestamp']

	class Meta:
		model = NodeStats

admin.site.register(NodeStats,NodeModelAdmin)
admin.site.register(NodeData)