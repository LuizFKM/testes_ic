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

        
        if download:
            os.makedirs(download_dir, exist_ok=True)
        
        resultados = []
        
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
                    filename = os.path.join(download_dir, os.path.basename(url))
                    with requests.get(url, stream=True) as response:
                        response.raise_for_status()
                        with open(filename, 'wb') as f:
                            for chunk in response.iter_content(8192):
                                f.write(chunk)
                    result['local_path'] = filename
                    result['success'] = True
                
                except Exception as e:
                    print(f"Erro ao baixar {url}: {str(e)}")
            
            resultados.append(result)
        return resultados
    
    def zip_anexos(self, anexos_dir='anexos', zip_name='anexos.zip', remove_after=False):
        zip_path = os.path.join(anexos_dir, zip_name)
        if not os.path.exists(anexos_dir):
            raise FileNotFoundError(f"Diretório '{anexos_dir}' não encontrado")
        if not os.listdir(anexos_dir):
            raise ValueError(f"Diretório '{anexos_dir}' está vazio")
        
        try:
            with ZipFile(zip_path, 'w', ZIP_DEFLATED) as zipf:
                for root, _, files in os.walk(anexos_dir):
                    for file in files:
                        if file != zip_name: 
                            file_path = os.path.join(root, file)
                            arcname = os.path.relpath(file_path, anexos_dir)
                            zipf.write(file_path, arcname)
                            
            if remove_after:
                for root, _, files in os.walk(anexos_dir):
                    for file in files:
                        if file != zip_name:
                            os.remove(os.path.join(root, file))
                            
            return os.path.abspath(zip_path)
            
        except Exception as e:
            if os.path.exists(zip_path):
                os.remove(zip_path)
            raise RuntimeError(f"Erro ao criar arquivo ZIP: {str(e)}")
        
        
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





