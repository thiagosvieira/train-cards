from rest_framework.viewsets import ModelViewSet
from treinamento.models import Instrutor
from treinamento.serializers import InstrutorSerializer

class InstrutorViewSet(ModelViewSet):
    queryset = Instrutor.objects.all()
    serializer_class = InstrutorSerializer

    