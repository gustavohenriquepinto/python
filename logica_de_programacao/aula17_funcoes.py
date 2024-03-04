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

x = 'Olá, mundo!'

def escopo():
    global x
    x = 4
    def funcao_interna():
        y = 7
        print(x + y)

    
    print(x)
    
    funcao_interna()

print(x)
escopo()
print(x)