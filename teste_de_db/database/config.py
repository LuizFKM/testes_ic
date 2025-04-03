import os
from pathlib import Path


BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
PATH_CSV = os.path.join(BASE_DIR, "arquivos_ptII")


ARQUIVOS_TABELAS = {
    "1T2023.csv": "dados_contabeis",
    "1T2024.csv": "dados_contabeis",
    "2T2023.csv": "dados_contabeis",
    "2T2024.csv": "dados_contabeis",
    "3T2023.csv": "dados_contabeis",
    "3T2024.csv": "dados_contabeis",
    "4T2023.csv": "dados_contabeis",
    "4T2024.csv": "dados_contabeis",
    "Relatorio_cadop.csv": "operadoras"
}


COLUNAS_TABELAS = {
    "dados_contabeis": (
        "data_inicio_trimestre", "registro_ans", "cd_conta_contabil", 
        "descricao", "vl_saldo_inicial", "vl_saldo_final"
    ),
    "operadoras": (
        "registro_ans", "cnpj", "razao_social", "nome_fantasia", 
        "modalidade", "logradouro", "numero", "complemento", 
        "bairro", "cidade", "uf", "cep", "ddd", "telefone", 
        "fax", "endereco_eletronico", "representante", 
        "cargo_representante", "regiao_de_comercializacao", 
        "data_registro_ans"
    )
}