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

    """
    Uso de recursividade
    """
    def filter_archive(self, columns: list, parameters: list):
        if len(columns) != len(parameters):
            raise ValueError ("Quantidade divergente de valores entre colunas e atributos")

        if len(columns) == 0:
            return self.df
        
        coluna_atual = columns[0]
        parametro_atual = parameters[0]

        df_filtrado = self.df[self.df[coluna_atual] == parametro_atual]
        
        if len(columns) == 1:
            return df_filtrado
        else:
            return self.filter_archive(columns[1:],parameters[1:])
        

path = './arquivo_teste.csv'
coluna = 'nome'
parametro = 'Produto A'

arquivo_csv = CsvProcessor(path)
arquivo_csv.read_archive()
print(arquivo_csv.filter_archive(coluna, parametro))