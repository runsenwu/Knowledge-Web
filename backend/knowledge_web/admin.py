from django.contrib import admin

# Register your models here.
from knowledge_web.models import Node, Edge

admin.site.register(Node)
admin.site.register(Edge)
admin.site.register(Graph)