from django.urls import path, include
from rest_framework import routers, serializers, viewsets
from . import views
from .models import Cycle
from .models import Goal
from .models import RoadBlock
from .models import RootCase


# Serializers define the API representation.
class CycleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cycle
        exclude = []


# ViewSets define the view behavior.
class CycleViewSet(viewsets.ModelViewSet):
    queryset = Cycle.objects.all()
    serializer_class = CycleSerializer


class GoalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Goal
        fields = ['id', 'title', 'cycle']


class GoalViewSet(viewsets.ModelViewSet):
    queryset = Goal.objects.all()
    serializer_class = GoalSerializer


class RoadBlockSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RoadBlock
        exclude = []


class RoadBlockViewSet(viewsets.ModelViewSet):
    queryset = RoadBlock.objects.all()
    serializer_class = RoadBlockSerializer


class DiagnoseRootCaseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RootCase
        exclude = []


class DiagnoseRootCaseViewSet(viewsets.ModelViewSet):
    queryset = RootCase.objects.all()
    serializer_class = DiagnoseRootCaseSerializer


router = routers.DefaultRouter()
router.register(r'cycles', CycleViewSet)
router.register(r'goal', GoalViewSet)
router.register(r'road_block', RoadBlockViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
