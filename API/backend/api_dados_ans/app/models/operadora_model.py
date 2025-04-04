from django.db import models

class Operadora(models.Model):
    registro_ans = models.CharField(max_length=6, unique=True, primary_key=True) 
    cnpj = models.CharField(max_length=14, unique=True)
    razao_social = models.CharField(max_length=140)
    nome_fantasia = models.CharField(max_length=140, blank=True, null=True)
    modalidade = models.CharField(max_length=40)
    logradouro = models.CharField(max_length=40, blank=True, null=True)
    numero = models.CharField(max_length=20, blank=True, null=True)
    complemento = models.CharField(max_length=40, blank=True, null=True)
    bairro = models.CharField(max_length=30, blank=True, null=True)
    cidade = models.CharField(max_length=30)
    uf = models.CharField(max_length=2)
    cep = models.CharField(max_length=8, blank=True, null=True)
    ddd = models.CharField(max_length=4, blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    fax = models.CharField(max_length=20, blank=True, null=True)
    endereco_eletronico = models.EmailField(max_length=255, blank=True, null=True)
    representante = models.CharField(max_length=50, blank=True, null=True)
    cargo_representante = models.CharField(max_length=40, blank=True, null=True)
    regiao_de_comercializacao = models.IntegerField(blank=True, null=True)
    data_registro_ans = models.DateField()
    
    class Meta:
            db_table = "operadoras" 


    def __str__(self):
        return f"{self.nome_fantasia or self.razao_social} ({self.registro_ans})"
