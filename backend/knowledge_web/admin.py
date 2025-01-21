from django.contrib import admin

# Register your models here.
from knowledge_web.models import Node, Relationship

admin.site.register(Node)
admin.site.register(Relationship)