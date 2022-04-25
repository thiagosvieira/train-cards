from os import defpath
from rest_framework import serializers
from .models import *


class TurnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turno
        fields = ["id","descricao", "horario"]
        read_only = True                          
class DiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dia
        fields = ["id","descricao"]
        read_only = True            
class TecnicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tecnica
        fields = ["id","descricao"]
        read_only = True          
class InstrutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instrutor
        fields = "__all__"
        read_only = True

class ObjetivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Objetivo
        fields = ["id","descricao"]
        read_only = True        



class Treinamento_ExercicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Treinamento_Exercicio
        fields = "__all__"

class Treinamento_ExercicioDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Treinamento_Exercicio
        fields = "__all__"
        depth = 2
class Treinamento_ExercicioVisuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Treinamento_Exercicio
        fields = ['exercicio','qtd_rep', 'qtd_set', 'intervalo','tecnicas']
        depth = 2
class TreinamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Treinamento
        fields = "__all__"
        read_only = True     

class TreinamentoDetailSerializer(serializers.ModelSerializer):
    exercicios = Treinamento_ExercicioVisuSerializer(many=True)
    class Meta:
        model = Treinamento
        fields = ['id','descricao','turnos', 'dias', 'exercicios']
        read_only = True 
        depth = 2

class ExercicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercicio
        fields = "__all__"
                 

class ExercicioDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercicio
        fields = "__all__"
        
        depth = 2


class FichaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ficha
        fields = "__all__" 
        read_only = True
class FichaDetailSerializer(serializers.ModelSerializer):
    treinamentos =TreinamentoDetailSerializer(many=True)
    class Meta:
        model = Ficha
        fields = ['id', 'objetivo', 'instrutor', 'user','data_criacao', 'atual','treinamentos']
        read_only = True
        depth = 3 #Exbi o detalhe dos objetos do json que são foreign key de acordo com a profundidade informada
    
    