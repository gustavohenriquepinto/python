# Try / Except

# Try -> Tenta executar um código.
# Except -> Ocorreu um erro ao executar um código.

numero = input('Digite um número: ')

try:
    print(f'{numero=}')
    
    print(f'O dobro de {float(numero)} é {float(numero) * 2}')
except:
    print('Você digitou algum caractere inválido')



# if numero.isdigit():
#     print(f'{numero=}')
#     print(f'O dobro de {float(numero)} é {float(numero) * 2}')
# else:
#     print('Você digitou algum caractere inválido')