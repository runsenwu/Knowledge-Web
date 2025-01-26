from rest_framework import serializers
from knowledge_web.models import Graph, Node, Edge

class GraphSerializer(serializers.HyperlinkedModelSerializer):
    nodes = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='node-detail')
    edges = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='edge-detail')

    class Meta:
        model = Graph
        fields = ['url', 'id', 'name', 'description', 'created_at', 'updated_at', 'nodes', 'edges']

class NodeSerializer(serializers.HyperlinkedModelSerializer):
    graph_id = serializers.HyperlinkedRelatedField(read_only=True, view_name='graph-detail')
    class Meta:
        model = Node
        fields = ['url', 'id', 'graph_id', 'name', 'description', 'position_x', 'position_y', 'node_type', 'created_at', 'updated_at']

class EdgeSerializer(serializers.HyperlinkedModelSerializer):
    graph_id = serializers.HyperlinkedRelatedField(read_only=True, view_name='graph-detail')
    starting_node = serializers.HyperlinkedRelatedField(read_only=True, view_name='node-detail')
    ending_node = serializers.HyperlinkedRelatedField(read_only=True, view_name='node-detail')
    class Meta:
        model = Edge
        fields = ['url', 'id', 'graph_id', 'starting_node', 'ending_node', 'description', 'connection_type', 'created_at', 'updated_at']
