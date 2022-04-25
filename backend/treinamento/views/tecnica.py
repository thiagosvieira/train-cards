from rest_framework.viewsets import ModelViewSet
from treinamento.models import Tecnica
from treinamento.serializers import TecnicaSerializer

class TecnicaViewSet(ModelViewSet):
    queryset = Tecnica.objects.all()
    serializer_class = TecnicaSerializer