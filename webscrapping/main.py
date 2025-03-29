from scraper import Scrapping

def main():
    url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"

    config = {
        'download': True,
        'compactar': True,
        'anexos_dir': 'anexos',
        'zip_name': 'anexos_ans.zip',
        'remove_after': True
    }

    scraper = Scrapping(url)
    anexos, zip_path = scraper.processar_anexos(**config)

    print(f"{len(anexos)} anexos baixados com sucesso")
    if zip_path and isinstance(zip_path, str):
        print(f" - Endereço dos arquivos: {zip_path}")
    
    elif isinstance(zip_path, str):
        print(f"- Erro na compactação: {zip_path}")

if __name__ == "__main__":
    main()
