# numero_inteiro = input('Digite um número inteiro: ')

# if(numero_inteiro.isdigit() and int(numero_inteiro) == float(numero_inteiro)):
#     print(f'Você digitou um número {'par' if int(numero_inteiro) % 2 == 0 else 'ímpar'}.')
# else:
#     print('Você precisa digitar um número inteiro.')

# ---------------------------------------------

# str_hora_atual = input('Informe a hora atual: ')

# def horario_do_dia(hora, comeco, fim) -> bool:
#     return hora >= comeco and hora < fim

# if str_hora_atual.isdigit():
#     int_hora_atual = int(str_hora_atual)
#     if horario_do_dia(int_hora_atual, 6, 12):
#         print('Bom dia!')
#     elif horario_do_dia(int_hora_atual, 12, 18):
#         print('Boa tarde!')
#     elif horario_do_dia(int_hora_atual, 18, 24) or horario_do_dia(int_hora_atual, 0, 6):
#         print('Boa noite!')
#     else:
#         print('Você não digtou um horário válido!')
# else:
#     print('Você não digtou um horário válido!')

# ---------------------------------------------

nome : str = input('Digite seu nome: ')

def nome_valido(texto : str) -> bool:

    caracteres_perimitidos : str = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'
    
    for letra in caracteres_perimitidos:
        if letra in texto:
            texto.replace(letra, '', 1)
            print('Ok')
    
    print(texto)
    return True if texto == '' else False

if len(nome) > 1 and not nome.isdigit():
    if len(nome) <= 4:
        print('Seu nome é curto.')
    elif len(nome) <= 6:
        print('Seu nome é curto.')
    else:
        print('Seu nome é longo')
else:
    print('Digite apenas letras e não deixe espaços em branco.')