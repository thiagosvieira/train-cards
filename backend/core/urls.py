from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from rest_framework import routers
from treinamento.views import instrutor, ficha, objetivo, treinamento, tecnica, dia, turno, exercicio

schema_view = get_schema_view(
    openapi.Info(
        title="Training Cards API",
        default_version="v1",
        description="Swagger UI to the Training Cards API",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@training_cards.com.br"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

router = routers.DefaultRouter()
router.register(r'instrutores', instrutor.InstrutorViewSet)
router.register(r'fichas', ficha.FichaViewSet)
router.register(r'objetivos', objetivo.ObjetivoViewSet)
router.register(r'treinamentos', treinamento.TreinamentoViewSet)
router.register(r'tecnicas', tecnica.TecnicaViewSet)
router.register(r'dias', dia.DiaViewSet)
router.register(r'turnos', turno.TurnoViewSet)
router.register(r'exercicios', exercicio.ExercicioViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
   
    path("api/", include('treinamento.urls'))
]
