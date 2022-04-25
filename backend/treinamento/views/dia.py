from rest_framework.viewsets import ModelViewSet
from treinamento.models import Dia
from treinamento.serializers import DiaSerializer

class DiaViewSet(ModelViewSet):
    queryset = Dia.objects.all()
    serializer_class = DiaSerializer

