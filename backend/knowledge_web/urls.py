from django.urls import path, include
from rest_framework.routers import DefaultRouter
from knowledge_web import views

router = DefaultRouter()
router.register(r'graphs', views.NodeViewSet, basename='graph')
router.register(r'nodes', views.NodeViewSet, basename='node')
router.register(r'edges', views.EdgeViewSet, basename='edge')

urlpatterns = [
    path('', include(router.urls)),
]
