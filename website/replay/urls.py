from django.urls import path, include
from rest_framework import routers, serializers, viewsets
from . import views
from .models import Cycle
from .models import Goal
from .models import RoadBlock
from .models import RootCase
from rest_framework.authentication import SessionAuthentication, BasicAuthentication


class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening


class CloseCsrfViewSet(viewsets.ModelViewSet):
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)


# Serializers define the API representation.
class CycleSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Cycle
        fields = ['id', 'title']


# ViewSets define the view behavior.
class CycleViewSet(CloseCsrfViewSet):
    queryset = Cycle.objects.all()
    serializer_class = CycleSerializer


class GoalSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Goal
        fields = ['id', 'title', 'cycle']


class GoalViewSet(CloseCsrfViewSet):

    queryset = Goal.objects.all()
    serializer_class = GoalSerializer


class RoadBlockSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RoadBlock
        exclude = []


class RoadBlockViewSet(CloseCsrfViewSet):
    queryset = RoadBlock.objects.all()
    serializer_class = RoadBlockSerializer


class DiagnoseRootCaseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RootCase
        exclude = []


class DiagnoseRootCaseViewSet(CloseCsrfViewSet):
    queryset = RootCase.objects.all()
    serializer_class = DiagnoseRootCaseSerializer


router = routers.DefaultRouter()
router.register(r'cycles', CycleViewSet)
router.register(r'goal', GoalViewSet)
router.register(r'road_block', RoadBlockViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('cycle/<id>', views.cycle)
]
