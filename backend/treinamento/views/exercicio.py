from rest_framework.viewsets import ModelViewSet
from treinamento.models import Exercicio
from treinamento.serializers import ExercicioSerializer, ExercicioDetailSerializer

class ExercicioViewSet(ModelViewSet):
    queryset = Exercicio.objects.all()
    serializer_class = ExercicioSerializer

    def get_serializer_class(self):
        if self.action == "list" or self.action == "retrieve":
            return ExercicioDetailSerializer
        else:
            return ExercicioSerializer        