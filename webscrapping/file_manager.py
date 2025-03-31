import os
from zipfile import ZipFile, ZIP_DEFLATED

class FileManager:
    @staticmethod
    def zip_files(anexos_dir='anexos', zip_name='anexos.zip', remove_after=False):
        base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        anexos_dir = os.path.join(base_dir, anexos_dir)
        zip_path = os.path.join(anexos_dir, zip_name)

        if not os.path.exists(anexos_dir):
            raise FileNotFoundError(f"Diretório '{anexos_dir}'não existe")
        
        if not os.listdir(anexos_dir):
            raise ValueError(f"Diretório '{anexos_dir}' não possui arquivos")
        
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
            raise e
        