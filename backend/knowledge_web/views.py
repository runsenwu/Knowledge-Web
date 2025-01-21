from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404

from django.http import HttpResponse
from django.template import loader

from .models import Node, Relationship

def index(request):
    node_list = Node.objects.order_by("node_name")[:5]
    context = {
        "node_list": node_list,
    }
    return render(request, "knowledge_web/index.html", context)

def node_detail(request, node_id):
    node = get_object_or_404(Node, pk=node_id)
    return render(request, "knowledge_web/node_detail.html", {"node": node})

def relationship_detail(request, relationship_id):
    relationship = get_object_or_404(Relationship, pk=relationship_id)
    return render(request, "knowledge_web/relationship_detail.html", {"relationship": relationship})