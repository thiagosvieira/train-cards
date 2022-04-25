from rest_framework.viewsets import ModelViewSet
from treinamento.models import Ficha
from treinamento.serializers import FichaSerializer, FichaDetailSerializer

class FichaViewSet(ModelViewSet):
    queryset = Ficha.objects.all()
    
    def get_serializer_class(self):
        if self.action == "list" or self.action == "retrieve":
            return FichaDetailSerializer
        else:
            return FichaSerializer    

    