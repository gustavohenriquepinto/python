import pandas as pd

data = pd.read_csv('~/dev/python/pandas/datasets/GasPricesinBrazil_2004-2019.csv', sep = ';')

# print(data['ESTADO'])
# print(data.iloc[0])
#
#product_reference = data['PRODUTO'] 
#product_copy = data['PRODUTO'].copy()
#
#data['PRODUTO'] = 'Hello, world!'
#
#print(data['PRODUTO'])
#print(product_reference)
#print(product_copy)

#data_rows, data_cols = data.shape
#
#produtos = [f'Produto {i}' for i in range(data_rows)]
#print(produtos)

print(list(data.index))
