 # While executa um código enquanto uma condição for verdadeira.

# condicao : int = 0

# while condicao <= 100:
#     condicao += 1

#     if condicao % 3 == 0:
#         continue

#     print(condicao)

#     if condicao == 40:
#         break

# print('\nSaiu do while.\n')

# qtd_linhas : int = 5
# qtd_colunas : int = 5

# linha : int = 1

# while linha <= qtd_linhas:
    
#     coluna : int = 1
#     while coluna <= qtd_colunas:
        
#         if coluna < qtd_colunas:
#             print(f'[{linha} , {coluna}]', end=' ')
#         else:
#             print(f'[{linha} , {coluna}]')
#         coluna += 1
    
#     linha += 1

# print('Fim.')

# nome : str = input('Qual é o seu primeiro nome? ')
# apelido : str = ''
# caractere : int = 0

# if nome.isalpha():
#     while caractere < len(nome):
#         apelido += '*' + nome[caractere] + ('' if caractere != len(nome) -1 else '*')
#         caractere += 1

#     print(f'Seu apelido é {apelido}.')
# else:
#     print('Seu nome pode conter apenas letras, e não deve estar em branco.')

# while True:
#     numero1 : float = 0
#     numero2 : float = 0
#     operacao : str = ''

#     try:
#         numero1 = float(input('Digite o primeiro número: '))
#         numero2 = float(input('Digite o segundo número: '))
#     except:
#         print('\nVocê digitou um número inválido.\n')
#         continue

#     operacao = input('Digite a operação (+-*/): ')
#     if operacao not in '+-*/' or len(operacao) > 1:
#         print('\nVocê digitou uma operação inválida.\n')
#         continue

#     print('O resultado da operação é:', end=' ')
#     if operacao == '+':
#         print(numero1 + numero2)
#     elif operacao == '-':
#         print(numero1 - numero2)
#     elif operacao == '*':
#         print(numero1 * numero2)
#     elif operacao == '/':
#         print(numero1 / numero2)
#     else:
#         print('Um erro inesperado.')
    
#     if input('Digite [S] para sair: ').lower().startswith('s'):
#         break

# frase : str = input('Digite uma frase: ')

# i = 0
# letra_mais_usada = ''
# int_letra_mais_usada = 0

# while i < len(frase):
#     if int_letra_mais_usada < frase.count(frase[i]) and frase[i] != ' ':
#         letra_mais_usada = frase[i]
#         int_letra_mais_usada = frase.count(frase[i])

#     if int_letra_mais_usada + i > len(frase) - 1:
#         break
    
#     i += 1

# print(f'A letra mais comum no texto é "{letra_mais_usada}", que aparece {int_letra_mais_usada} vezes.')

# texto = 'Maria'

# for caractere in texto:
#     print(caractere)

# numeros = range(10)
# numeros = range(5, 10)
# numeros = range(15, 3, -1)

# for numero in numeros:
#     print(numero)