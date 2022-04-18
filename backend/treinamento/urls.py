from .views import *
from django.urls import path

urlpatterns = [
    path("instrutores/", InstrutorList.as_view()),
    path("instrutor/<int:id>/", InstrutorDetail.as_view()),
    path("objetivos/", ObjetivoList.as_view()),
    path("objetivo/<int:id>/", ObjetivoDetail.as_view()), 
    path("fichas/", FichaList.as_view()),
    path("fichas/usuario/<int:id>/", FichaListUsuario.as_view()),    
    path("ficha/<int:id>/", FichaDetail.as_view()),     
    path("ficha/usuario/<int:id>/ficha-atual", FichaUsuarioAtual.as_view()),    
    path("treinamentos/", TreinamentoList.as_view()),
    path("treinamento/<int:id>/", TreinamentoDetail.as_view()),
    path("turnos/", TurnoList.as_view()),
    path("turno/<int:id>/", TurnoDetail.as_view()),              
    path("dias/", DiaList.as_view()),
    path("dia/<int:id>/", DiaDetail.as_view()),                  
    path("exercicios/", ExercicioList.as_view()),
    path("exercicio/<int:id>/", ExercicioDetail.as_view()),                  
    path("tecnicas/", TecnicaList.as_view()),
    path("tecnica/<int:id>/", TecnicaDetail.as_view()),                      
    path("fichas_treinamentos/", Ficha_TreinamentoList.as_view()),
    path("ficha_treinamento/<int:id>/", Ficha_TreinamentoDetail.as_view()),
    path("treinamentos_turno/", Treinamento_TurnoList.as_view()),
    path("treinamento_turno/<int:id>/", Treinamento_TurnoDetail.as_view()),
    path("treinamentos_dia/", Treinamento_DiaList.as_view()),
    path("treinamento_dia/<int:id>/", Treinamento_DiaDetail.as_view()),    
    path("treinamentos_exercicio/", Treinamento_ExercicioList.as_view()),
    path("treinamento_exercicio/<int:id>/", Treinamento_ExercicioDetail.as_view()),        
    path("treinamentos_exercicio_tecnica/", Treinamento_Exercicio_TecnicaList.as_view()),
    path("treinamento_exercicio_tecnica/<int:id>/", Treinamento_Exercicio_TecnicaDetail.as_view()),            
                        

]
