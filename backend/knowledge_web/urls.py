from django.urls import path, include
from rest_framework.routers import DefaultRouter
from knowledge_web.views import GraphViewSet, NodeViewSet, EdgeViewSet

router = DefaultRouter()
router.register(r'graphs', GraphViewSet)
router.register(r'nodes', NodeViewSet)
router.register(r'edges', EdgeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
