import requests
from bs4 import BeautifulSoup

class Scrapping(object):
    def __init__(self, url):
        self.url = url
        self.soup = self._get_soup()

    def _get_soup(self):
        response = requests.get(self.url)
        response.raise_for_status()
        return BeautifulSoup(response.text, "html.parser")

    def get_anexos_links(self):
        lista_links = self.soup.find_all('a', class_='internal-link')
        return list(map(lambda link: link.get('href'), filter(lambda link: 'Anexo I.' in link.text or 'Anexo II.' in link.text, lista_links )))