
from rest_framework import viewsets, filters
from app.models import Operadora
from app.serializers import OperadoraSerializer
from rest_framework.pagination import PageNumberPagination

class OperadoraPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 5

class OperadoraViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Operadora.objects.all().order_by('nome_fantasia')
    serializer_class = OperadoraSerializer
    pagination_class = OperadoraPagination
    
    filter_backends = [filters.SearchFilter]
    search_fields = [
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
    def get_queryset(self):
        if not self.request.query_params.get('search'):
            return Operadora.objects.none()
            
        return Operadora.objects.all().order_by('nome_fantasia')

