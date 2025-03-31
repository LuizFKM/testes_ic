import pdfplumber
import os
import csv
import tabula


class TransformaDados(object):
    def __init__(self, arquivo: str, csv_saida: str):
        self.arquivo = arquivo
        self.csv_saida = csv_saida
        self.tabelas = self._extrair_tabelas()
        self.colunas = self._extrair_nome_colunas()

    def _extrair_tabelas(self):
        tabelas = []
        with pdfplumber.open(self.arquivo) as pdf:
            for page_num in range(min(4, len(pdf.pages))):  
                page = pdf.pages[page_num]
                tabelas = page.extract_table()
                if tabelas:
                    tabelas.append(tabelas)  
            return tabelas
    
    def _extrair_nome_colunas(self):
        if self.tabelas:
            cabecalho = self.tabelas[0]
            print(cabecalho)
            return cabecalho
        return[]



    
    

    # def _salvar_csv(self, rn_vigentes):
    #     with open(self.csv_saida, mode="w", newline="", encoding="utf8") as arquivo_csv:
    #         salvar_csv = csv.writer(arquivo_csv)
    #         salvar_csv.writerow(["RN vigentes"])
    #         for linha in rn_vigentes:
    #             salvar_csv.writerow([linha])
