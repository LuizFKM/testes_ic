from extracao_dados import TransformaDados
import os



def main():
    caminho_conteudo =  os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "anexos"))
    caminho_pdf = os.path.join(caminho_conteudo, 'Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf')
    conteudo_csv = "Anexo I.csv"

    if not os.path.exists(caminho_conteudo):
        print(f"Erro: A pasta 'anexos' não foi encontrada no caminho: {caminho_conteudo}")
        return

    if not os.path.exists(caminho_pdf):
        print(f"Erro: O PDF '{caminho_pdf}' não foi encontrado.")
        return

    extrair = TransformaDados(caminho_pdf, conteudo_csv)

    print(f"Concluído. Arquivo salvo em: {conteudo_csv}")

if __name__ == "__main__":
    main()
