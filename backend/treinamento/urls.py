from django.urls import path, include
from rest_framework import routers
from treinamento.views import instrutor, ficha, objetivo, treinamento, tecnica, dia, turno, exercicio, treinamento_exercicio


router = routers.DefaultRouter()
router.register(r'instrutores', instrutor.InstrutorViewSet)
router.register(r'fichas', ficha.FichaViewSet)
router.register(r'objetivos', objetivo.ObjetivoViewSet)
router.register(r'treinamentos', treinamento.TreinamentoViewSet)
router.register(r'tecnicas', tecnica.TecnicaViewSet)
router.register(r'dias', dia.DiaViewSet)
router.register(r'turnos', turno.TurnoViewSet)
router.register(r'exercicios', exercicio.ExercicioViewSet)
router.register(r'treinamento_exercicios', treinamento_exercicio.Treinamento_ExercicioViewSet) 

urlpatterns = [
    path("", include(router.urls))
]
