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

# lista_nomes = ['Maria', 'Helena', 'Luiz']
# indices = range(len(lista_nomes))

# for indice in indices:
#     print(indice, lista_nomes[indice])

# _, nome2, *_ = ['Maria', 'Gustavo', 'Henrique']

# nomes = 'Gustavo', 'Henrique', 'Maria'
# nomes = tuple(['Maria', 'Gustavo', 'Henrique'])

# print(nomes)

# lista = ['Gustavo', 'Henrique', 'Silva']
# lista.append('João')

# for indice, nome in enumerate(lista):
#     print(indice, nome)

# print(list(enumerate(lista)))


# lista = []

# while True:
#     print('Selecione uma opção: ')
#     acao = input('[i]nserir, [a]pagar, [l]istar, [e]ncerrar: ')[0].lower()

#     match acao:
#         case 'e':
#             break

#         case 'i':
#             novo_item = input('Digite o item a ser inserido na lista: ')

#             if not novo_item.isdigit:
#                 print('Seeu item não pode ser um número!\n')
#             else:
#                 lista.append(novo_item)

#         case 'a':
#             if len(lista) == 0:
#                 print('Sua lista não contém nenhum item para apagar!\n')
#                 continue

#             for indice, nome in enumerate(lista):
#                 print(indice, nome)
            
#             item_para_apagar = input(f'\nDigite o índice do item a ser apagado na lista, um número de 0 a {len(lista) - 1}: ')

#             if item_para_apagar.isdigit():
#                 if int(item_para_apagar) >= 0 and int(item_para_apagar) <= len(lista) - 1:
#                     del lista[int(item_para_apagar)]
#                 else:
#                     print('Este não é um índice da lista!\n')
#             else:
#                 print('Você precisa digitar um número!\n')

#         case 'l':
#             if len(lista) == 0:
#                 print('Sua lista não contém nenhum item para listar!\n')
#                 continue

#             for indice, nome in enumerate(lista):
#                 print(indice, nome)
#             print('')

#         case _:
#             print('Você digitou uma ação inválida!\n')

