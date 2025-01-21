from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("node/<int:node_id>", views.node_detail, name="node_detail"),
    path("relationship/<int:relationship_id>", views.relationship_detail, name="relationship_detail"),
]