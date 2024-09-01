import pandas as pd

#x = int(input('Lines: '))
data = pd.read_csv('~/dev/python/pandas/datasets/GasPricesinBrazil_2004-2019.csv', sep = ';')

print('Tabela completa:', data, sep='\n')
#print(f'Primeiros {x} lançamentos da tabela:', data.head(x))
#print('Dados da tabela:', data.info(), sep='\n')
#print('Tipo de variável:', type(data))
#print('Linhas e colunas:', data.shape)
