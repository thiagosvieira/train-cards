from rest_framework.viewsets import ModelViewSet
from treinamento.models import Turno
from treinamento.serializers import TurnoSerializer

class TurnoViewSet(ModelViewSet):
    queryset = Turno.objects.all()
    serializer_class = TurnoSerializer