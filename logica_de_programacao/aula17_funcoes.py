# def o_que_e_funcao() -> str:
#     return 'Funções são trechos de código  usados para replicar ações.'

# def escreva_o_que_e_funcao() -> None:
#     print(o_que_e_funcao())

# def isso_e_um_numero(texto_numero : str) -> bool:
#     return texto_numero.isnumeric()

# def numero_retorno(usuario : str) -> int:
#     if 'a' in usuario:
#         return 1243
#     return 0

# escreva_o_que_e_funcao()

# if isso_e_um_numero('2f3'):
#     escreva_o_que_e_funcao()
# else:
#     print('Seu número é', numero_retorno(input('Digite: ')))

# def somar(x : int = 0, y : int = 0, z : object = None):
#     if z is None:
#         print(f'{x=} + {y=} -> ', x + y)
#     else:
#         print(f'{x=} + {y=} + {z=} -> ', x + y + z)

# somar(1,2)

# x = 'Olá, mundo!'

# def escopo():
#     global x
#     x = 4
#     def funcao_interna():
#         y = 7
#         print(x + y)

    
#     print(x)
    
#     funcao_interna()

# print(x)
# escopo()
# print(x)

# def soma(*numeros):
#     total = 0
#     for numero in numeros:
#         total += numero
    
#     return total

# print(soma(3, -4, 5, -20, 64))

# def criar_saudacao(saudacao, nome):
#     def saudar():
#         return f'{saudacao}, {nome}!'
#     return saudar

# nova_saudacao = criar_saudacao('Bom dia', 'Gustavo')

# print(nova_saudacao())

# def multiplicar(fator):
#     def calcular(numero):
#         return numero * fator
    
#     return calcular

# duplicar = multiplicar(2)
# triplicar = multiplicar(3)
# quadruplicar = multiplicar(4)

# print(duplicar(3))
# print(triplicar(-1))
# print(quadruplicar(4.5))