from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
# this is where the data principles will be stored, it will keep track of the state
#   and also the relationships between different data models

class Node(models.Model):
    node_name = models.CharField(max_length=200)

    def __str__(self):
        return self.node_name

class Relationship(models.Model):
    parent = models.ForeignKey(Node, on_delete=models.CASCADE, related_name="children")
    child = models.ForeignKey(Node, on_delete=models.CASCADE, related_name="parents")
    description = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.child.node_name + " -> " + self.parent.node_name
