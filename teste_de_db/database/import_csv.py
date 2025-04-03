import csv
import logging
from db_connection import DatabaseConnection
from config import COLUNAS_TABELAS

class DataProcessor:
    def __init__(self, file_path, table_name, columns, delimiter=";"):
        self.file_path = file_path
        self.table_name = table_name
        self.columns = columns
        self.delimiter = delimiter

    def clean_data(self, value):

        if value is None or str(value).strip() == "":
            return None
        return str(value).strip().strip('"')

    def process_operadoras_row(self, linha):

        uf_index = self.columns.index("uf")
        linha[uf_index] = linha[uf_index][:2] if linha[uf_index] else None
        return linha

    def process_dados_contabeis_row(self, linha):

        if len(linha) >= 6:
            linha[4] = linha[4].replace(",", ".")  
            linha[5] = linha[5].replace(",", ".")  
        return linha

    def process_row(self, linha):

        linha = [self.clean_data(col) for col in linha]
        

        registro_index = self.columns.index("registro_ans")
        linha[registro_index] = linha[registro_index].strip()


        if self.table_name == "operadoras":
            linha = self.process_operadoras_row(linha)
        elif self.table_name == "dados_contabeis":
            linha = self.process_dados_contabeis_row(linha)
            
        return tuple(linha)

    def import_to_postgres(self):

        try:
            with DatabaseConnection.get_connection() as conn:
                with conn.cursor() as cur:
                    with open(self.file_path, mode="r", encoding="utf8") as arquivo:
                        reader = csv.reader(arquivo, delimiter=self.delimiter)
                        next(reader) 
                        
                        cleaned_data = [self.process_row(linha) for linha in reader]
                        
                        if cleaned_data:
                            query = f"""
                                INSERT INTO {self.table_name} 
                                ({', '.join(self.columns)}) 
                                VALUES ({', '.join(['%s'] * len(self.columns))})
                            """
                            cur.executemany(query, cleaned_data)
                            conn.commit()
                            logging.info(f"Importados {len(cleaned_data)} registros para {self.table_name}")
                        else:
                            logging.warning("Nenhum registro válido para importação")
        
        except Exception as e:
            logging.error(f"Erro ao inserir dados na tabela {self.table_name}: {e}")
            if conn:
                conn.rollback()