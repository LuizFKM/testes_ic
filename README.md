# Documentação do Sistema de Web Scraping e Gerenciamento de Arquivos ANS

## Visão Geral do Sistema
Este sistema integrado realiza duas funções principais:
1. **Coleta de Dados**: Web scraping de anexos do portal da ANS (Agência Nacional de Saúde Suplementar)
2. **Transformação de Dados**: Processamento dos PDFs baixados para gerar datasets estruturados em CSV

## Estrutura de Arquivos
```
pasta_webscraping/
├── file_manager.py   # Classe para gerenciamento de arquivos
├── main.py           # Script principal de execução
└── scraper.py        # Classe principal de web scraping
```

## 1. file_manager.py

### Classe `FileManager`
Responsável por operações de gerenciamento de arquivos, principalmente compactação.

#### Método `zip_files`
Compacta arquivos em um diretório para um arquivo ZIP.

**Parâmetros:**
- `anexos_dir` (str): Diretório contendo os arquivos a serem compactados (padrão: 'anexos')
- `zip_name` (str): Nome do arquivo ZIP de saída (padrão: 'anexos.zip')
- `remove_after` (bool): Se True, remove os arquivos originais após compactação (padrão: False)

**Retorno:**
- Caminho absoluto do arquivo ZIP criado

**Exceções:**
- `FileNotFoundError`: Se o diretório especificado não existir
- `ValueError`: Se o diretório estiver vazio
- `Exception`: Qualquer outro erro durante o processo (o arquivo ZIP parcial é removido)

**Comportamento:**
1. Verifica a existência do diretório e se contém arquivos
2. Cria um arquivo ZIP com todos os arquivos do diretório
3. Remove os arquivos originais se `remove_after=True`
4. Retorna o caminho absoluto do ZIP criado

## 2. main.py

### Função `main()`
Ponto de entrada do programa, configura e executa o web scraping.

**Fluxo:**
1. Define a URL alvo (site da ANS)
2. Configura parâmetros:
   - `download`: Habilita download dos arquivos
   - `compactar`: Habilita compactação dos downloads
   - `anexos_dir`: Diretório para salvar arquivos
   - `zip_name`: Nome do arquivo ZIP
   - `remove_after`: Não remove arquivos após compactação
3. Cria instância do `Scrapping` e processa os anexos
4. Exibe resultados:
   - Número de anexos baixados
   - Caminho do arquivo ZIP ou mensagem de erro

## 3. scraper.py

### Classe `Scrapping`
Realiza o web scraping e download dos anexos.

#### Método `__init__(self, url)`
Inicializa o scraper com a URL alvo.

#### Método `_get_soup(self)`
Obtém e parseia o conteúdo HTML da URL usando BeautifulSoup.

#### Método `get_anexos(self, download=True, download_dir='anexos')`
Encontra e baixa os anexos da página.

**Parâmetros:**
- `download`: Se True, baixa os arquivos encontrados
- `download_dir`: Diretório para salvar os downloads

**Retorno:**
- Lista de dicionários com informações sobre cada anexo:
  - `url`: URL do anexo
  - `local_path`: Caminho local do arquivo baixado (None se não baixado)
  - `success`: Status do download

**Fluxo:**
1. Encontra todos os links com classe 'internal-link'
2. Filtra apenas links contendo 'Anexo I.' ou 'Anexo II.' no texto
3. Baixa cada arquivo (se habilitado)
4. Retorna estatísticas e tempo de execução

#### Método `processar_anexos(self, download=True, compactar=True, **kwargs)`
Coordena o processo completo de obtenção e compactação de anexos.

**Parâmetros:**
- `download`: Habilita download dos arquivos
- `compactar`: Habilita compactação dos downloads
- `**kwargs`: Argumentos adicionais para `FileManager.zip_files()`

**Retorno:**
- Tupla contendo:
  - Lista de resultados dos downloads
  - Caminho do arquivo ZIP ou mensagem de erro (se aplicável)

## Fluxo do Sistema
1. `main.py` inicia o processo com as configurações definidas
2. `Scrapping` obtém a página web e filtra os anexos relevantes
3. Os anexos são baixados para o diretório especificado
4. `FileManager` compacta os arquivos baixados (se habilitado)
5. Os resultados são exibidos no console

## Dependências
- requests: Para requisições HTTP
- BeautifulSoup (bs4): Para parsing HTML
- os, zipfile: Para operações de arquivo
- time: Para medição de tempo de execução
- urllib.parse: Para manipulação de URLs

## Exemplo de Uso
```python
# Configuração básica
config = {
    'download': True,
    'compactar': True,
    'anexos_dir': 'anexos',
    'zip_name': 'anexos_ans.zip',
    'remove_after': False
}

# Execução
scraper = Scrapping("https://www.gov.br/ans/...")
anexos, zip_path = scraper.processar_anexos(**config)
```

# Sistema de Transformação de Dados

## Visão Geral
Responsável por extrair dados de arquivos PDF (especificamente anexos da ANS), transformá-los em DataFrames pandas, realizar limpeza e transformações, e exportar para formatos como CSV e ZIP.

## Estrutura de Arquivos
```
transformacao_dados/
├── extracao_dados.py  # Classe principal de transformação de dados
└── main.py            # Script principal de execução
```

## 1. extracao_dados.py

### Classe `TransformaDados`
Responsável por toda a transformação de dados de PDF para CSV.

#### Método `__init__(self, arquivo: str, csv_saida: str)`
Inicializa o processador com:
- `arquivo`: Caminho do PDF a ser processado
- `csv_saida`: Diretório de saída para os arquivos CSV

#### Métodos Principais:

1. **`_extrair_tabelas(self)`**
   - Extrai todas as tabelas do PDF usando pdfplumber
   - Retorna lista de tabelas (cada tabela é uma lista de linhas)

2. **`_extrair_nome_colunas(self)`**
   - Extrai o cabeçalho da primeira tabela encontrada

3. **`_extrair_linhas(self)`**
   - Extrai todas as linhas de dados das tabelas

4. **`_limpa_dado(self, dado)`**
   - Remove quebras de linha e espaços excessivos dos dados

5. **`converte_para_dataFrame(self)`**
   - Converte os dados extraídos em um DataFrame pandas
   - Realiza limpeza (remove linhas vazias, valores NA)

6. **`renomear_colunas(self, mapeamento_colunas: dict)`**
   - Renomeia colunas conforme mapeamento fornecido
   - Exemplo: {'OD': 'Seg. Odontológica'}

7. **`salvar_para_csv(self)`**
   - Salva o DataFrame em arquivo CSV com formatação específica:
     - Encoding UTF-8 com BOM
     - Todos os valores entre aspas
     - Delimitador ponto-e-vírgula

8. **`compactar_csv(self, caminho_csv: str, nome_zip: str, remove_after: bool)`**
   - Compacta o CSV gerado em arquivo ZIP
   - Opcionalmente remove arquivos originais (CSV e PDFs no diretório)

## 2. main.py

### Função `main()`
Ponto de entrada do programa, configura e executa a transformação de dados.

**Fluxo:**
1. Define caminhos dos arquivos:
   - Verifica existência da pasta 'anexos' e do PDF
2. Configura mapeamento de renomeação de colunas
3. Cria instância de `TransformaDados` com:
   - Arquivo PDF de entrada
   - Diretório de saída
4. Executa transformações:
   - Renomeia colunas conforme mapeamento
   - Salva como CSV
   - Compacta o resultado
5. Remove arquivos temporários se configurado

## Dependências
- `pdfplumber`: Para extração de tabelas de PDF
- `pandas`: Para manipulação de dados em DataFrames
- `zipfile`: Para compactação de arquivos
- `os`, `csv`: Para operações de sistema e arquivos

## Fluxo de Processamento
1. Extrai todas as tabelas do PDF
2. Identifica cabeçalhos e linhas de dados
3. Limpa e formata os dados
4. Converte para DataFrame pandas
5. Renomeia colunas conforme especificado
6. Exporta para CSV com formatação padronizada
7. Compacta o CSV em arquivo ZIP
8. Opcionalmente remove arquivos intermediários

## Exemplo de Uso
```python
# Configuração básica
mapeamento = {
    'OD': 'Seg. Odontológica',
    'AMB': 'Seg. Ambulatorial'
}

# Processamento
processador = TransformaDados(
    arquivo='caminho/para/Anexo_I.pdf',
    csv_saida='caminho/saida'
)

processador.renomear_colunas(mapeamento)
caminho_csv = processador.salvar_para_csv()

if caminho_csv:
    processador.compactar_csv(caminho_csv, 'arquivo_saida', remove_after=True)
```

