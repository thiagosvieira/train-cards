from rest_framework.viewsets import ModelViewSet
from treinamento.models import Treinamento
from treinamento.serializers import TreinamentoSerializer, TreinamentoDetailSerializer

class TreinamentoViewSet(ModelViewSet):
    queryset = Treinamento.objects.all()
    

    def get_serializer_class(self):
        if self.action == "list" or self.action == "retrieve":
            return TreinamentoDetailSerializer
        else:
            return TreinamentoSerializer   