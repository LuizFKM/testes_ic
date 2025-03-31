import time
from urllib.parse import urljoin
from zipfile import ZIP_DEFLATED, ZipFile
import requests
import os
from bs4 import BeautifulSoup
from file_manager import FileManager


class Scrapping(object):
    def __init__(self, url):
        self.url = url
        self.soup = self._get_soup()
        self.file_manager = FileManager()

    def _get_soup(self):
        response = requests.get(self.url)
        response.raise_for_status()
        return BeautifulSoup(response.text, "html.parser")

    def get_anexos(self, download=True, download_dir='anexos'):
        lista_links = self.soup.find_all('a', class_='internal-link')
        anexos_links = list(filter(lambda link: 'Anexo I.' in link.text or 'Anexo II.' in link.text, lista_links))

        projeto_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        download_path = os.path.join(projeto_dir, download_dir)
        
        if download:
            os.makedirs(download_path, exist_ok=True)
        
        resultados = []
        start_time = time.time()
        
        for link in anexos_links:
            url = link.get('href')
            if not url:
                continue
            if not url.startswith(('http://', 'https://')):
                url = urljoin(self.url, url)
            result = {
                'url': url,
                'local_path': None,
                'success': False
            }

            if download:
                try:
                    filename = os.path.join(download_path, os.path.basename(url))
                    with requests.get(url, stream=True, timeout=10) as response:
                        response.raise_for_status()
                        with open(filename, 'wb') as f:
                            for chunk in response.iter_content(65536):
                                f.write(chunk)
                    result['local_path'] = filename
                    result['success'] = True
                
                except Exception as e:
                    print(f"Erro ao baixar {url}: {str(e)}")
            
            resultados.append(result)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Download concluído em {elapsed_time:.2f} segundos.")
        return resultados
        
        
    def processar_anexos(self, download=True, compactar=True, **kwargs):
        resultados = []

        for anexo in self.get_anexos(download=download):
            if download and anexo['success']:
                resultados.append(anexo)

    
        if download and compactar and resultados:
            try:
                zip_path = self.file_manager.zip_files(**kwargs)
                return resultados, zip_path  
            except Exception as e:
                return resultados, str(e)  

        return resultados, None
    