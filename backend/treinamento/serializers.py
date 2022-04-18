from rest_framework import serializers
from .models import *

class InstrutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instrutor
        fields = ["id","nome"]
        read_only = True

class ObjetivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Objetivo
        fields = ["id","descricao"]
        read_only = True        

class FichaSerializer(serializers.ModelSerializer):
    id_objetivo = ObjetivoSerializer(read_only = True)
    id_instrutor = InstrutorSerializer(read_only = True)
    # id_user = UserSerializer

    class Meta:
        model = Ficha
        fields = ["id","id_objetivo","id_instrutor","id_user","data_criacao","atual"]
        read_only = True      

class FichaCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ficha
        fields = ["id","id_objetivo","id_instrutor","id_user","data_criacao","atual"]
        read_only = True 


class TreinamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Treinamento
        fields = ["id","descricao"]
        read_only = True                     

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


class ExercicioCompostoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercicio
        fields = ["id","descricao","is_composto","id_exercicio_composto"]
        read_only = True


class ExercicioSerializer(serializers.ModelSerializer):
    id_exercicio_composto = ExercicioCompostoSerializer(read_only = True)
    
    class Meta:
        model = Exercicio
        fields = ["id","descricao","is_composto","id_exercicio_composto"]
        read_only = True         

class ExercicioCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercicio
        fields = ["id","descricao","is_composto","id_exercicio_composto"]
        read_only = True


class Ficha_TreinamentoSerializer(serializers.ModelSerializer):
    id_ficha = FichaSerializer(read_only = True)
    id_treinamento = TreinamentoSerializer(read_only = True)

    class Meta:
        model = Ficha_Treinamento
        fields = ["id","id_ficha","id_treinamento"]
        read_only = True 
        
class Ficha_TreinamentoCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ficha_Treinamento
        fields = ["id","id_ficha","id_treinamento"]
        read_only = True 


class Treinamento_TurnoSerializer(serializers.ModelSerializer):
    id_treinamento = TreinamentoSerializer(read_only = True)
    id_turno = TurnoSerializer(read_only = True)

    class Meta:
        model = Treinamento_Turno
        fields = ["id","id_treinamento","id_turno"]
        read_only = True 
        
class Treinamento_TurnoCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Treinamento_Turno
        fields = ["id","id_treinamento","id_turno"]
        read_only = True 

class Treinamento_DiaSerializer(serializers.ModelSerializer):
    id_treinamento = TreinamentoSerializer(read_only = True)
    id_dia = DiaSerializer(read_only = True)

    class Meta:
        model = Treinamento_Dia
        fields = ["id","id_treinamento","id_dia"]
        read_only = True 
        
class Treinamento_DiaCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Treinamento_Dia
        fields = ["id","id_treinamento","id_dia"]
        read_only = True 


class Treinamento_ExercicioSerializer(serializers.ModelSerializer):
    id_treinamento = TreinamentoSerializer(read_only = True)
    id_exercicio = ExercicioSerializer(read_only = True)

    class Meta:
        model = Treinamento_Exercicio
        fields = ["id","id_treinamento","id_exercicio","qtd_rep","qtd_set","intervalo"]
        read_only = True 
        
class Treinamento_ExercicioCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Treinamento_Exercicio
        fields = ["id","id_treinamento","id_exercicio","qtd_rep","qtd_set","intervalo"]
        read_only = True 

class Treinamento_Exercicio_TecnicaSerializer(serializers.ModelSerializer):
    id_treinamento_exercicio = Treinamento_ExercicioSerializer(read_only = True)
    id_tecnica = TecnicaSerializer(read_only = True)

    class Meta:
        model = Treinamento_Exercicio_Tecnica
        fields = ["id","id_treinamento_exercicio","id_tecnica"]
        read_only = True 
        
class Treinamento_Exercicio_TecnicaCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Treinamento_Exercicio_Tecnica
        fields = ["id","id_treinamento_exercicio","id_tecnica"]
        read_only = True         