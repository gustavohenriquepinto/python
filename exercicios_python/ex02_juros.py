print('\nBem-vindo ao calculador de juros.')

montante : float = 0
capital : float = 0
tempo : float = 0
taxa : float = 0

texto_aplicacao = input('Qual o valor que deseja investir? ')

if texto_aplicacao.isdigit():
    capital = float(texto_aplicacao)
else:
    print('Você digitou algum caractere incorreto.')

texto_tempo = input('Por quantos meses deseja investir? ')

if texto_tempo.isdigit():
    tempo = float(texto_aplicacao)
else:
    print('Você digitou algum caractere incorreto.')

texto_taxa = input('Qual é a taxa efetiva mensal? ')
texto_regime = input('Qual será o regime de capitalização? [S]imples / [C]omposto: ')
