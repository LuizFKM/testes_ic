from scraper import Scrapping

url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
scraper = Scrapping(url)

print("Links anexos: ", scraper.get_anexos_links())