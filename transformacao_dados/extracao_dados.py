import zipfile
import pdfplumber
import os
import csv
import pandas as pd


class TransformaDados(object):
    def __init__(self, arquivo: str, csv_saida: str):
        self.arquivo = arquivo
        self.csv_saida = os.path.abspath(csv_saida)
        self.csv_saida = csv_saida
        self.tabelas = self._extrair_tabelas()
        self.colunas = self._extrair_nome_colunas()
        self.linhas = self._extrair_linhas()
        self.convercao_dataFrame = self.converte_para_dataFrame()


    def _extrair_tabelas(self):
        todas_tabelas = []
        with pdfplumber.open(self.arquivo) as pdf:
            for page_num in range(len(pdf.pages)):  
                page = pdf.pages[page_num]
                tabelas = page.extract_table()
                if tabelas:
                    todas_tabelas.append(tabelas)  
        return todas_tabelas
    
    def _extrair_nome_colunas(self):
        if self.tabelas and len(self.tabelas) > 0:
            cabecalho = self.tabelas[0][0]

        return cabecalho  
        
            
    
    def _extrair_linhas(self):
        linhas  = []
        if self.tabelas:
            for tabela in self.tabelas:
                linhas.extend(tabela[1:])
        return linhas
    
    def _limpa_dado(self,dado):
        if isinstance(dado, str):
            dado = ' '.join(dado.replace('\n', ' ').split()).strip()
        return dado
    
    def converte_para_dataFrame(self):
        try:
            linhas_limpas = [[self._limpa_dado(cell) for cell in row] for row in self.linhas]
            df = pd.DataFrame(linhas_limpas, columns=self.colunas)
            df.replace('', pd.NA, inplace=True)
            df.dropna(how='all', inplace=True)

            pd.set_option('display.max_colwidth', 40)
            pd.set_option('display.width', 1000)
            return df
        
        except Exception as e:
            print(f"Erro ao criar DataFrame: {str(e)}")
            return pd.DataFrame()
    
    
    
    def renomear_colunas(self, mapeamento_colunas: dict):
        if self.convercao_dataFrame is not None:
            try:
                self.convercao_dataFrame.columns = self.convercao_dataFrame.columns.str.strip()
                self.convercao_dataFrame.columns = self.convercao_dataFrame.columns.str.replace('\n', ' ')
                self.convercao_dataFrame = self.convercao_dataFrame.rename(columns=mapeamento_colunas)
                self.colunas = list(self.convercao_dataFrame.columns)
                print("Colunas renomeadas com sucesso!")
                print(f"Novos nomes: {list(self.convercao_dataFrame.columns)}")
            except Exception as e:
                print(f"Erro ao renomear colunas: {str(e)}")
    
    def salvar_para_csv(self):
        df = self.convercao_dataFrame
        nome_arquivo = "Anexo_I.csv"
        caminho_csv = os.path.join(self.csv_saida, nome_arquivo)
        if df is not None:
            try:
                df = df.map(lambda x: f' {x} ' if pd.notna(x) else x)
                df.to_csv(caminho_csv, index=False, encoding='utf-8-sig', quoting=csv.QUOTE_ALL, quotechar='"', escapechar="\\", lineterminator="\r\n",  sep=';')
                print(f"CSV salvo em: {caminho_csv}")
                return caminho_csv
            except Exception as e:
                print(f"Erro ao salvar: {str(e)}")
        return False
    
    def compactar_csv(self, caminho_csv: str, nome_zip: str,  remove_after: bool = False) -> str:
        if not os.path.exists(caminho_csv):
            print(f"Erro: Arquivo CSV '{caminho_csv}' não encontrado para compactação.")
            return ""

        caminho_zip = os.path.join(self.csv_saida, f"{nome_zip}.zip")

        try:
            with zipfile.ZipFile(caminho_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
                zipf.write(caminho_csv, os.path.basename(caminho_csv))

            if remove_after:
                try:
                    os.remove(caminho_csv)
                    print(f"Arquivo CSV original removido: {caminho_csv}")
                    
                    pdfs_removidos = set()
                    for arquivo in os.listdir(self.csv_saida):
                        if arquivo.lower().endswith('.pdf'):
                            pdf_path = os.path.join(self.csv_saida, arquivo)
                            try:
                                os.remove(pdf_path)
                                pdfs_removidos.add(pdf_path)
                            except Exception as e:
                                print(f"Erro ao remover PDF {pdf_path}: {str(e)}")
                    
                except Exception as e:
                    print(f"Aviso: Não foi possível remover o arquivo CSV: {str(e)}")


            print(f"Arquivo compactado em: {caminho_zip}")
            return caminho_zip

        except Exception as e:
            print(f"Erro ao compactar arquivo: {str(e)}")
            return ""