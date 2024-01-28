# lista = [123, True, 'Gustavo Henrique', 1.2, []]

# lista[-3] = 'Pedro'
# del lista[2]

# lista.append('Olá, mundo!')
# string_ola_mundo = lista.pop()
# # print(string_ola_mundo)

# # lista.clear()

# lista.insert(0,'Isso é uma string!')


# print(lista, type(lista), sep='\n')

# lista_a = [1,2,3]
# lista_b = [4,5,6]

# lista_c = lista_a + lista_b
# lista_a.extend(lista_b)

# print(lista_a, lista_b, lista_c, sep='\n')

# lista_a = [1,2,3]
# lista_b = ['Gustavo', 'Henrique', 'Silva']

# lista_a.pop()
# print(lista_b)

# for nome in lista_b:
#     for letra in nome:
#         print(letra, end='_')
#     print('')

lista_nomes = ['Maria', 'Helena', 'Luiz']
indices = range(len(lista_nomes))

for indice in indices:
    print(indice, lista_nomes[indice])