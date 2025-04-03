import logging
from config import ARQUIVOS_TABELAS, COLUNAS_TABELAS, PATH_CSV
from import_csv import DataProcessor
import os

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

def process_files():

    process_table("operadoras")
    
    process_table("dados_contabeis")

def process_table(table_name):

    for arquivo, tabela in ARQUIVOS_TABELAS.items():
        if tabela == table_name:
            caminho_csv = os.path.join(PATH_CSV, arquivo)
            
            if os.path.exists(caminho_csv):
                processor = DataProcessor(
                    file_path=caminho_csv,
                    table_name=tabela,
                    columns=COLUNAS_TABELAS[tabela]
                )
                processor.import_to_postgres()
            else:
                logging.warning(f"Arquivo não encontrado: {caminho_csv}")

if __name__ == "__main__":
    setup_logging()
    process_files()