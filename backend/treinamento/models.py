from django.db import models

from authentication.models import UserAccount


# Create your models here.

class  Instrutor(models.Model):
    nome = models.CharField(unique=True, max_length=255)

    class Meta:
        db_table = "instrutor"

    def __str__(self):
        return self.nome
        
    
class Objetivo(models.Model):
    descricao = models.CharField(unique=True, max_length=255)

    class Meta:
        db_table = "objetivo"

    def __str__(self):
        return self.descricao    

class Turno (models.Model):
    descricao = models.CharField(max_length=255, unique=True)
    horario = models.IntegerField()

    class Meta:
        db_table = "turno"

    def __str__(self):
        return self.descricao        

class Dia (models.Model):
    descricao = models.CharField(max_length=255, unique=True)

    class Meta:
        db_table = "dia"

    def __str__(self):
        return self.descricao        

class Tecnica (models.Model):
    descricao = models.CharField(max_length=255, unique=True)

    class Meta:
        db_table = "tecnica"

    def __str__(self):
        return self.descricao     
class Exercicio (models.Model):
    descricao = models.CharField(max_length=255)
    is_composto = models.BooleanField(default=False)
    id_exercicio_composto = models.ForeignKey(
        'self',
        related_name="exercicios",
        on_delete= models.PROTECT,
        db_column="id_exercicio_composto",
        null=True
    )

    class Meta:
        unique_together = (("descricao", "is_composto"),) 
        db_table = "exercicio"

    def __str__(self):
        return self.descricao        
      

class Treinamento (models.Model):
    descricao = models.CharField(max_length=255)
    turnos = models.ManyToManyField(Turno)
    dias = models.ManyToManyField(Dia)
    
    class Meta:
        db_table = "treinamento"

    def __str__(self):
        return self.descricao

class Treinamento_Exercicio (models.Model):
    treinamento = models.ForeignKey(
        Treinamento,
        related_name="exercicios",
        on_delete= models.CASCADE,
        db_column="id_treinamento"
    )
    exercicio = models.ForeignKey(
        Exercicio,
        related_name="treinamento_exercicio",
        on_delete= models.PROTECT,
        db_column="id_exercicio"
    )
    qtd_rep = models.IntegerField(default=12)
    qtd_set = models.IntegerField(default=12)
    intervalo = models.CharField(max_length=255, default="40 sec")   
    tecnicas = models.ManyToManyField(Tecnica)
    class Meta:
        db_table = "treinamento_exercicio"            


class Ficha(models.Model):
    id_objetivo = models.ForeignKey(
        Objetivo,
        related_name="fichas",
        on_delete= models.PROTECT,
        db_column="id_objetivo"
    )
    id_instrutor = models.ForeignKey(
        Instrutor,
        related_name="fichas",
        on_delete= models.PROTECT,
        db_column="id_instrutor"
    )
    id_user = models.ForeignKey(
        UserAccount,
        related_name="fichas",
        on_delete= models.PROTECT,
        db_column="id_user"
    )    
    data_criacao = models.DateTimeField(
        auto_now_add=True,
        editable=False 
    )

    atual = models.BooleanField(default=False)

    treinamentos = models.ManyToManyField(Treinamento)
    
    class Meta:
        db_table = "ficha"
