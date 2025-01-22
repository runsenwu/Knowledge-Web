from rest_framework import serializers
from knowledge_web.models import Graph, Node, Edge

class GraphSerializer(serializers.ModelSerializer):
    nodes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    edges = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Graph
        fields = ['id', 'name', 'description', 'created_at', 'updated_at', 'nodes', 'edges']

class NodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Node
        fields = ['id', 'graph_id', 'name', 'description', 'position_x', 'position_y', 'node_type', 'created_at', 'updated_at']

class EdgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Edge
        fields = ['id', 'graph_id', 'starting_node', 'ending_node', 'description', 'connection_type', 'created_at', 'updated_at']
