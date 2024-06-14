import pandas as pd

class CsvProcessor:
    """ 
    Classe para processamento de arquivos CSV
    """
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.df = None

    def read_archive(self):
        self.df = pd.read_csv(self.file_path)

    def filter_archive(self, column: str, parameter: list):
        return self.df[self.df[column] == parameter]
        

path = './arquivo_teste.csv'
coluna = 'nome'
parametro = 'Produto A'

arquivo_csv = CsvProcessor(path)
arquivo_csv.read_archive()
print(arquivo_csv.filter_archive(coluna, parametro))