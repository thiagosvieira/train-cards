from django.db import models

from authentication.models import UserAccount


# Create your models here.

class  Instrutor(models.Model):
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(unique=True, max_length=255)

    class Meta:
        db_table = "instrutor"

    def __str__(self):
        return self.nome
        
    
class Objetivo(models.Model):
    id = models.IntegerField(primary_key=True)
    descricao = models.CharField(unique=True, max_length=255)

    class Meta:
        db_table = "objetivo"

    def __str__(self):
        return self.descricao    

class Ficha(models.Model):
    id = models.IntegerField(primary_key=True)
    id_objetivo = models.ForeignKey(
        Objetivo,
        related_name="id_objetivo",
        on_delete= models.PROTECT,
        db_column="id_objetivo"
    )
    id_instrutor = models.ForeignKey(
        Instrutor,
        related_name="id_instrutor",
        on_delete= models.PROTECT,
        db_column="id_instrutor"
    )
    id_user = models.ForeignKey(
        UserAccount,
        related_name="id_user",
        on_delete= models.PROTECT,
        db_column="id_user"
    )    
    data_criacao = models.DateTimeField(
        auto_now_add=True,
        editable=False 
    )
    
    class Meta:
        db_table = "ficha"

     
class Treinamento (models.Model):
    id = models.IntegerField(primary_key=True)
    descricao = models.CharField(max_length=255)

    class Meta:
        db_table = "treinamento"

    def __str__(self):
        return self.descricao

class Turno (models.Model):
    id = models.IntegerField(primary_key=True)
    descricao = models.CharField(max_length=255, unique=True)
    horario = models.IntegerField()

    class Meta:
        db_table = "turno"

    def __str__(self):
        return self.descricao        

class Dia (models.Model):
    id = models.IntegerField(primary_key=True)
    descricao = models.CharField(max_length=255, unique=True)

    class Meta:
        db_table = "dia"

    def __str__(self):
        return self.descricao        

class Exercicio (models.Model):
    id = models.IntegerField(primary_key=True)
    descricao = models.CharField(max_length=255, unique=True)
    is_composto = models.BooleanField(default=False)
    id_exercicio_composto = models.ForeignKey(
        'self',
        related_name="E_exercicio_composto",
        on_delete= models.PROTECT,
        db_column="id_exercicio_composto",
        null=True
    )

    class Meta:
        db_table = "exercicio"

    def __str__(self):
        return self.descricao        

class Tecnica (models.Model):
    id = models.IntegerField(primary_key=True)
    descricao = models.CharField(max_length=255, unique=True)

    class Meta:
        db_table = "tecnica"

    def __str__(self):
        return self.descricao        

class Ficha_Treinamento (models.Model):
    id = models.IntegerField(primary_key=True)
    
    id_ficha = models.ForeignKey(
        Ficha,
        related_name="FT_ficha",
        on_delete= models.CASCADE,
        db_column="id_ficha"
    )
    id_treinamento = models.ForeignKey(
        Treinamento,
        related_name="FT_treinamento",
        on_delete= models.PROTECT,
        db_column="id_treinamento"
    )    

    class Meta:
        unique_together = (("id_ficha", "id_treinamento"),)  
        db_table = "ficha_treinamento"      

class Treinamento_Turno (models.Model):
    id = models.IntegerField(primary_key=True)
    
    id_treinamento = models.ForeignKey(
        Treinamento,
        related_name="TT_treinamento",
        on_delete= models.CASCADE,
        db_column="id_treinamento"
    )
    id_turno = models.ForeignKey(
        Turno,
        related_name="TT_turno",
        on_delete= models.PROTECT,
        db_column="id_turno"
    )    

    class Meta:
        unique_together = (("id_treinamento", "id_turno"),)  
        db_table = "treinamento_turno"           

class Treinamento_Dia (models.Model):
    id = models.IntegerField(primary_key=True)
    
    id_treinamento = models.ForeignKey(
        Treinamento,
        related_name="TD_treinamento",
        on_delete= models.CASCADE,
        db_column="id_treinamento"
    )
    id_dia = models.ForeignKey(
        Dia,
        related_name="TD_dia",
        on_delete= models.PROTECT,
        db_column="id_dia"
    )    

    class Meta:
        unique_together = (("id_treinamento", "id_dia"),)  
        db_table = "treinamento_dia"           

class Treinamento_Exercicio (models.Model):
    id = models.IntegerField(primary_key=True)
    
    id_treinamento = models.ForeignKey(
        Treinamento,
        related_name="TE_treinamento",
        on_delete= models.CASCADE,
        db_column="id_treinamento"
    )
    id_exercicio = models.ForeignKey(
        Exercicio,
        related_name="TE_exercicio",
        on_delete= models.PROTECT,
        db_column="id_exercicio"
    )   
 
    class Meta:
        db_table = "treinamento_exercicio"            

class Treinamento_Exercicio_Tecnica (models.Model):
    id = models.IntegerField(primary_key=True)
    
    id_treinamento_exercicio = models.ForeignKey(
        Treinamento,
        related_name="TET_treinamento_exercicio",
        on_delete= models.CASCADE,
        db_column="id_treinamento_exercicio"
    )
    id_tecnica = models.ForeignKey(
        Exercicio,
        related_name="TET_tecnica",
        on_delete= models.PROTECT,
        db_column="id_tecnica"
    )   

    class Meta:
        db_table = "treinamento_exercicio_tecnica"        