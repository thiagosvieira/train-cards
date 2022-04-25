from rest_framework.viewsets import ModelViewSet
from treinamento.models import Objetivo
from treinamento.serializers import ObjetivoSerializer

class ObjetivoViewSet(ModelViewSet):
    queryset = Objetivo.objects.all()
    serializer_class = ObjetivoSerializer

    