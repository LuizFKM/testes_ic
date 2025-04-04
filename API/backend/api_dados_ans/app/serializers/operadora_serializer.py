from rest_framework import serializers
from app.models import Operadora

class OperadoraSerializer(serializers.ModelSerializer):
    nome_empresa = serializers.SerializerMethodField()
    
    class Meta:
        model = Operadora
        fields = [
            'registro_ans',
            'cnpj',
            'razao_social', 
            'nome_fantasia', 
            'modalidade',
            'logradouro',
            'numero',
            'complemento',
            'bairro',
            'cidade',
            'uf',
            'cep',
            'ddd',
            'telefone',
            'fax',
            'endereco_eletronico',
            'representante',
            'cargo_representante',
            'regiao_de_comercializacao',
            'data_registro_ans'
        ]
    
    def get_nome_empresa(self, obj):
        return obj.nome_fantasia if obj.nome_fantasia else obj.razao_social