from extracao_dados import TransformaDados
import os



def main():
    base_dir = os.path.dirname(__file__)
    caminho_anexos = os.path.abspath(os.path.join(base_dir, "..", "anexos"))
    caminho_pdf = os.path.join(caminho_anexos, 'Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf')

    

    if not os.path.exists(caminho_anexos):
        print(f"Erro: A pasta 'anexos' não foi encontrada no caminho: {caminho_anexos}")
        return

    if not os.path.exists(caminho_pdf):
        print(f"Erro: O PDF '{caminho_pdf}' não foi encontrado.")
        return
    
    mapeamento = {
    'OD': 'Seg. Odondologica',
    'AMB': 'Seg. Ambulatorial',
    
}
    processador = TransformaDados(
        arquivo=caminho_pdf,
        csv_saida=caminho_anexos
    )

    processador.renomear_colunas(mapeamento_colunas=mapeamento)
    caminho_csv = processador.salvar_para_csv()


    if caminho_csv:
        nome_zip = "Teste_Luiz_Francisco"
        caminho_zip = processador.compactar_csv(caminho_csv, nome_zip, remove_after=True)


if __name__ == "__main__":
    main()
