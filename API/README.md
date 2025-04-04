# API de Operadoras ANS - Resumo

## **Endpoints Principais**
### 1. Listar Operadoras
`GET /api/operadoras`  
**Parâmetros**:  
- `search`: Termo de busca (obrigatório)  
- `page`: Número da página  
- `page_size`: Itens por página (máx 5)  

**Exemplo**:  
`GET /api/operadoras?search=saude&page=2`

### 2. Detalhes da Operadora
`GET /api/operadoras/{registro_ans}`  
**Exemplo**:  
`GET /api/operadoras/123456`

## **Respostas**
**Formato Padrão**:
```json
{
  "count": 23,
  "next": "...",
  "previous": "...",
  "results": [{...}]
}
```

**Campos Principais**:
- `registro_ans`: ID único (6 dígitos)  
- `nome_empresa`: Nome comercial  
- `cnpj`: CNPJ sem formatação  
- `uf`: Estado de atuação  


## **Configuração Rápida**
```bash
# Variáveis de ambiente
export DB_NAME='db_name' DB_USER='user' DB_PASS='password'

# Comandos
python manage.py migrate
python manage.py runserver
```

## **Códigos HTTP**
| Código | Descrição          |
|--------|--------------------|
| 200    | Sucesso            |
| 400    | Busca inválida     |
| 404    | Não encontrado     |

## **Uso Básico**
```python
import requests

# Listagem
response = requests.get("http://localhost:8000/api/operadoras", 
                       params={"search": "saude"})

# Detalhes
response = requests.get("http://localhost:8000/api/operadoras/123456")
```

**Nota**: Campo `search` é obrigatório para evitar consultas vazias.
