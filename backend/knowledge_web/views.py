from rest_framework import viewsets
from rest_framework.response import Response
from knowledge_web.models import Graph, Node, Edge
from knowledge_web.serializers import GraphSerializer, NodeSerializer, EdgeSerializer
from rest_framework.views import APIView
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view

class GraphViewSet(viewsets.ModelViewSet):
    queryset = Graph.objects.all()
    serializer_class = GraphSerializer

class NodeViewSet(viewsets.ModelViewSet):
    queryset = Node.objects.all()
    serializer_class = NodeSerializer

class EdgeViewSet(viewsets.ModelViewSet):
    queryset = Edge.objects.all()
    serializer_class = EdgeSerializer
