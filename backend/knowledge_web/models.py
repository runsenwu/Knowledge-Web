from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils.timezone import now

# Create your models here.
# this is where the data principles will be stored, it will keep track of the state
#   and also the relationships between different data models

class Graph(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=500, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Node(models.Model):
    graph_id = models.ForeignKey(Graph, on_delete=models.CASCADE, related_name="nodes")
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=500, blank=True)
    position_x = models.FloatField(default=0.0)
    position_y = models.FloatField(default=0.0)
    node_type = models.CharField(max_length=50, default="round")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Edge(models.Model):
    graph_id = models.ForeignKey(Graph, on_delete=models.CASCADE, related_name="edges")
    starting_node = models.ForeignKey(Node, on_delete=models.CASCADE, related_name="start")
    ending_node = models.ForeignKey(Node, on_delete=models.CASCADE, related_name="end")
    description = models.CharField(max_length=500, blank=True)
    connection_type = models.CharField(max_length=50, default="line")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.starting_node.name + " --- " + self.ending_node.name
