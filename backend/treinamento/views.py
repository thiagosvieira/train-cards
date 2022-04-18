from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
import requests
from .models import *
from .serializers import *

'''
# Instrutor
'''
class InstrutorList(APIView):

    def get(self, request):
        queryset = Instrutor.objects.all()
        serializer = InstrutorSerializer(queryset, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=InstrutorSerializer())
    def post(self, request):
        serializer = InstrutorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)          

class InstrutorDetail(APIView):

    def get_object(self, id):
        try:
            return Instrutor.objects.get(id=id)
        except Instrutor.DoesNotExist:
            raise Http404

    def get(self, request, id):
        instrutor = self.get_object(id)
        serializer = InstrutorSerializer(instrutor)
        return Response(serializer.data)         

    @swagger_auto_schema(request_body=InstrutorSerializer())
    def put(self, request, id):
        instrutor = self.get_object(id)
        serializer = InstrutorSerializer(instrutor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)        

    def delete(self, request, id):
        instrutor = self.get_object(id)
        instrutor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 

'''
# Objetivo
'''
class ObjetivoList(APIView):

    def get(self, request):
        queryset = Objetivo.objects.all()
        serializer = ObjetivoSerializer(queryset, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=ObjetivoSerializer())
    def post(self, request):
        serializer = ObjetivoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)          

class ObjetivoDetail(APIView):

    def get_object(self, id):
        try:
            return Objetivo.objects.get(id=id)
        except Objetivo.DoesNotExist:
            raise Http404

    def get(self, request, id):
        objetivo = self.get_object(id)
        serializer = ObjetivoSerializer(objetivo)
        return Response(serializer.data)         

    @swagger_auto_schema(request_body=ObjetivoSerializer())
    def put(self, request, id):
        objetivo = self.get_object(id)
        serializer = ObjetivoSerializer(objetivo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)        

    def delete(self, request, id):
        objetivo = self.get_object(id)
        objetivo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 


'''
# Ficha
'''
class FichaList(APIView):

    def get(self, request):
        queryset = Ficha.objects.all()
        serializer = FichaSerializer(queryset, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=FichaCreateUpdateSerializer())
    def post(self, request):
        serializer = FichaCreateUpdateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)          

class FichaDetail(APIView):

    def get_object(self, id):
        try:
            return Ficha.objects.get(id=id)
        except Ficha.DoesNotExist:
            raise Http404

    def get(self, request, id):
        ficha = self.get_object(id)
        serializer = FichaSerializer(ficha)
        return Response(serializer.data)         

    @swagger_auto_schema(request_body=FichaCreateUpdateSerializer())
    def put(self, request, id):
        ficha = self.get_object(id)
        serializer = FichaCreateUpdateSerializer(ficha, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)        

    def delete(self, request, id):
        ficha = self.get_object(id)
        ficha.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 

#Lista de fichas por usuário
class FichaListUsuario(APIView):

    def get(self, request, id):
        queryset = Ficha.objects.filter(id_user__id=id)
        serializer = FichaSerializer(queryset, many=True)
        return Response(serializer.data)

#Ficha que o usuáiro está utilizando no momento        
class FichaUsuarioAtual(APIView):

    def get(self, request, id):
        queryset = Ficha.objects.filter(id_user__id=id).filter(atual=True)
        serializer = FichaSerializer(queryset, many=True)
        return Response(serializer.data)        


'''
# Treinamento
'''
class TreinamentoList(APIView):

    def get(self, request):
        queryset = Treinamento.objects.all()
        serializer = TreinamentoSerializer(queryset, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=TreinamentoSerializer())
    def post(self, request):
        serializer = TreinamentoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)          

class TreinamentoDetail(APIView):

    def get_object(self, id):
        try:
            return Treinamento.objects.get(id=id)
        except Treinamento.DoesNotExist:
            raise Http404

    def get(self, request, id):
        treinamento = self.get_object(id)
        serializer = TreinamentoSerializer(treinamento)
        return Response(serializer.data)         

    @swagger_auto_schema(request_body=TreinamentoSerializer())
    def put(self, request, id):
        treinamento = self.get_object(id)
        serializer = TreinamentoSerializer(treinamento, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)        

    def delete(self, request, id):
        treinamento = self.get_object(id)
        treinamento.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 


'''
# Turno
'''
class TurnoList(APIView):

    def get(self, request):
        queryset = Turno.objects.all()
        serializer = TurnoSerializer(queryset, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=TurnoSerializer())
    def post(self, request):
        serializer = TurnoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)          

class TurnoDetail(APIView):

    def get_object(self, id):
        try:
            return Turno.objects.get(id=id)
        except Turno.DoesNotExist:
            raise Http404

    def get(self, request, id):
        turno = self.get_object(id)
        serializer = TurnoSerializer(turno)
        return Response(serializer.data)         

    @swagger_auto_schema(request_body=TurnoSerializer())
    def put(self, request, id):
        turno = self.get_object(id)
        serializer = TurnoSerializer(turno, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)        

    def delete(self, request, id):
        turno = self.get_object(id)
        turno.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



'''
# Dia
'''
class DiaList(APIView):

    def get(self, request):
        queryset = Dia.objects.all()
        serializer = DiaSerializer(queryset, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=DiaSerializer())
    def post(self, request):
        serializer = DiaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)          

class DiaDetail(APIView):

    def get_object(self, id):
        try:
            return Dia.objects.get(id=id)
        except Dia.DoesNotExist:
            raise Http404

    def get(self, request, id):
        dia = self.get_object(id)
        serializer = DiaSerializer(dia)
        return Response(serializer.data)         

    @swagger_auto_schema(request_body=DiaSerializer())
    def put(self, request, id):
        dia = self.get_object(id)
        serializer = DiaSerializer(dia, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)        

    def delete(self, request, id):
        dia = self.get_object(id)
        dia.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

'''
# Exercicio
'''
class ExercicioList(APIView):

    def get(self, request):
        queryset = Exercicio.objects.all()
        serializer = ExercicioSerializer(queryset, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=ExercicioCreateUpdateSerializer())
    def post(self, request):
        serializer = ExercicioCreateUpdateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)          

class ExercicioDetail(APIView):

    def get_object(self, id):
        try:
            return Exercicio.objects.get(id=id)
        except Exercicio.DoesNotExist:
            raise Http404

    def get(self, request, id):
        exercicio = self.get_object(id)
        serializer = ExercicioSerializer(exercicio)
        return Response(serializer.data)         

    @swagger_auto_schema(request_body=ExercicioCreateUpdateSerializer())
    def put(self, request, id):
        exercicio = self.get_object(id)
        serializer = ExercicioCreateUpdateSerializer(exercicio, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)        

    def delete(self, request, id):
        exercicio = self.get_object(id)
        exercicio.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


'''
# Tecnica
'''
class TecnicaList(APIView):

    def get(self, request):
        queryset = Tecnica.objects.all()
        serializer = TecnicaSerializer(queryset, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=TecnicaSerializer())
    def post(self, request):
        serializer = TecnicaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)          

class TecnicaDetail(APIView):

    def get_object(self, id):
        try:
            return Tecnica.objects.get(id=id)
        except Tecnica.DoesNotExist:
            raise Http404

    def get(self, request, id):
        tecnica = self.get_object(id)
        serializer = TecnicaSerializer(tecnica)
        return Response(serializer.data)         

    @swagger_auto_schema(request_body=TecnicaSerializer())
    def put(self, request, id):
        tecnica = self.get_object(id)
        serializer = TecnicaSerializer(tecnica, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)        

    def delete(self, request, id):
        tecnica = self.get_object(id)
        tecnica.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



'''
# Ficha_Treinamento
'''
class Ficha_TreinamentoList(APIView):

    def get(self, request):
        queryset = Ficha_Treinamento.objects.all()
        serializer = Ficha_TreinamentoSerializer(queryset, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=Ficha_TreinamentoCreateUpdateSerializer())
    def post(self, request):
        serializer = Ficha_TreinamentoCreateUpdateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)          

class Ficha_TreinamentoDetail(APIView):

    def get_object(self, id):
        try:
            return Ficha_Treinamento.objects.get(id=id)
        except Ficha_Treinamento.DoesNotExist:
            raise Http404

    def get(self, request, id):
        ficha_treinamento = self.get_object(id)
        serializer = Ficha_TreinamentoSerializer(ficha_treinamento)
        return Response(serializer.data)         

    @swagger_auto_schema(request_body=Ficha_TreinamentoCreateUpdateSerializer())
    def put(self, request, id):
        ficha_treinamento = self.get_object(id)
        serializer = Ficha_TreinamentoCreateUpdateSerializer(ficha_treinamento, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)        

    def delete(self, request, id):
        ficha_treinamento = self.get_object(id)
        ficha_treinamento.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

'''
# Treinamento_Turno
'''
class Treinamento_TurnoList(APIView):

    def get(self, request):
        queryset = Treinamento_Turno.objects.all()
        serializer = Treinamento_TurnoSerializer(queryset, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=Treinamento_TurnoCreateUpdateSerializer())
    def post(self, request):
        serializer = Treinamento_TurnoCreateUpdateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)          

class Treinamento_TurnoDetail(APIView):

    def get_object(self, id):
        try:
            return Treinamento_Turno.objects.get(id=id)
        except Treinamento_Turno.DoesNotExist:
            raise Http404

    def get(self, request, id):
        treinamento_turno = self.get_object(id)
        serializer = Treinamento_TurnoSerializer(treinamento_turno)
        return Response(serializer.data)         

    @swagger_auto_schema(request_body=Treinamento_TurnoCreateUpdateSerializer())
    def put(self, request, id):
        treinamento_turno = self.get_object(id)
        serializer = Treinamento_TurnoCreateUpdateSerializer(treinamento_turno, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)        

    def delete(self, request, id):
        treinamento_turno = self.get_object(id)
        treinamento_turno.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

'''
# Treinamento_Dia
'''
class Treinamento_DiaList(APIView):

    def get(self, request):
        queryset = Treinamento_Dia.objects.all()
        serializer = Treinamento_DiaSerializer(queryset, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=Treinamento_DiaCreateUpdateSerializer())
    def post(self, request):
        serializer = Treinamento_DiaCreateUpdateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)          

class Treinamento_DiaDetail(APIView):

    def get_object(self, id):
        try:
            return Treinamento_Dia.objects.get(id=id)
        except Treinamento_Dia.DoesNotExist:
            raise Http404

    def get(self, request, id):
        treinamento_dia = self.get_object(id)
        serializer = Treinamento_DiaSerializer(treinamento_dia)
        return Response(serializer.data)         

    @swagger_auto_schema(request_body=Treinamento_DiaCreateUpdateSerializer())
    def put(self, request, id):
        treinamento_dia = self.get_object(id)
        serializer = Treinamento_DiaCreateUpdateSerializer(treinamento_dia, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)        

    def delete(self, request, id):
        treinamento_dia = self.get_object(id)
        treinamento_dia.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


'''
# Treinamento_Exercicio
'''
class Treinamento_ExercicioList(APIView):

    def get(self, request):
        queryset = Treinamento_Exercicio.objects.all()
        serializer = Treinamento_ExercicioSerializer(queryset, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=Treinamento_ExercicioCreateUpdateSerializer())
    def post(self, request):
        serializer = Treinamento_ExercicioCreateUpdateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)          

class Treinamento_ExercicioDetail(APIView):

    def get_object(self, id):
        try:
            return Treinamento_Exercicio.objects.get(id=id)
        except Treinamento_Exercicio.DoesNotExist:
            raise Http404

    def get(self, request, id):
        treinamento_exercicio = self.get_object(id)
        serializer = Treinamento_ExercicioSerializer(treinamento_exercicio)
        return Response(serializer.data)         

    @swagger_auto_schema(request_body=Treinamento_ExercicioCreateUpdateSerializer())
    def put(self, request, id):
        treinamento_exercicio = self.get_object(id)
        serializer = Treinamento_ExercicioCreateUpdateSerializer(treinamento_exercicio, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)        

    def delete(self, request, id):
        treinamento_exercicio = self.get_object(id)
        treinamento_exercicio.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


'''
# Treinamento_Exercicio_Tecnica
'''
class Treinamento_Exercicio_TecnicaList(APIView):

    def get(self, request):
        queryset = Treinamento_Exercicio_Tecnica.objects.all()
        serializer = Treinamento_Exercicio_TecnicaSerializer(queryset, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=Treinamento_Exercicio_TecnicaCreateUpdateSerializer())
    def post(self, request):
        serializer = Treinamento_Exercicio_TecnicaCreateUpdateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)          

class Treinamento_Exercicio_TecnicaDetail(APIView):

    def get_object(self, id):
        try:
            return Treinamento_Exercicio_Tecnica.objects.get(id=id)
        except Treinamento_Exercicio_Tecnica.DoesNotExist:
            raise Http404

    def get(self, request, id):
        treinamento_exercicio_tecnica = self.get_object(id)
        serializer = Treinamento_Exercicio_TecnicaSerializer(treinamento_exercicio_tecnica)
        return Response(serializer.data)         

    @swagger_auto_schema(request_body=Treinamento_Exercicio_TecnicaCreateUpdateSerializer())
    def put(self, request, id):
        treinamento_exercicio_tecnica = self.get_object(id)
        serializer = Treinamento_Exercicio_TecnicaCreateUpdateSerializer(treinamento_exercicio_tecnica, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)        

    def delete(self, request, id):
        treinamento_exercicio_tecnica = self.get_object(id)
        treinamento_exercicio_tecnica.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
