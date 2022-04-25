from rest_framework.viewsets import ModelViewSet
from treinamento.models import Treinamento_Exercicio
from treinamento.serializers import Treinamento_ExercicioSerializer, Treinamento_ExercicioDetailSerializer

class Treinamento_ExercicioViewSet(ModelViewSet):
    queryset = Treinamento_Exercicio.objects.all()
    

    def get_serializer_class(self):
        if self.action == "list" or self.action == "retrieve":
            return Treinamento_ExercicioDetailSerializer
        else:
            return Treinamento_ExercicioSerializer   