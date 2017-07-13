from rest_framework.serializers import ModelSerializer
from app.models import NodeStats,NodeData

class NodeStatsSerializers(ModelSerializer):
	class Meta:
		model = NodeStats
		fields = [
			'node_id',
			'name',
			'location',
			'timestamp',
		]

class NodeDataSerializers(ModelSerializer):
	class Meta:
		model = NodeData
		fields = [
			'pk',
			'node',
			'battery_str',
			'signal_str',
			'ctimestamp',
			'data'
		]
