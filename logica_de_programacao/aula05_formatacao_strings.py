# nome = 'Gustavo'
# idade = 19
# altura = 1.73

# print(f'{nome}, você tem {idade} anos e {altura:.2f} de altura')

# a = 'A'
# b = 'B'
# c = 1.1

# string = 'a={0} b={1} c={nome3:.2f} a = {1}'
# formato = string.format(a, b, nome3=c)

# print(formato)

# nome = input('Qual seu nome? ')
# print(f'Olá, {nome=}!')

# numero1 = int(input('Digite o primeiro número: '))
# numero2 = int(input('Digite o segundo número: '))

# print(f'A soma dos números é: {numero1+numero2}')

# ----------------------------------------------------

# s - string
# d ou i - int
# f - float
# x ou X - Hexadecimal

# nome = 'Gustavo'
# preco = 99.994775
# numero = 1267

# print('%s, o preço é de %.2f.' % (nome, preco))

# print('O hexadecimal de %i é %04x' % (numero, numero))

# ----------------------------------------------------

# texto = 'ABC'
# numero462 = 7574.756382123

# print(f'{texto}.')
# print(f'{texto: >10}.')
# print(f'{texto: <10}.')
# print(f'{texto: ^10}.')
# print(f'{texto:_<10}.')

# print(f'{numero:0=+20,.1f}')

# numero = int(numero)
# print(f'O hexadecimal de {numero} é {numero:06x}')

# ---------------------------------------------------

# Fatiamento de strings

# texto = 'Olá, mundo!'

# print(texto[0:11:2])
# print(texto[::-1])
# ----------------------------------------

nome = input('Digite seu nome: ')
letras_nome = 0

if nome:

    for letra in nome:
        letras_nome += 0 if letra==' ' else 1

    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
    print(f'Seu nome{' ' if ' ' in nome else ' não '}contém{f' {len(nome)-letras_nome} ' if ' ' in nome else ' '}espaços')
    print(f'Seu nome tem {letras_nome} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[-1]}')
else:
    print('Seu nome não pode ser um campo vazio.')