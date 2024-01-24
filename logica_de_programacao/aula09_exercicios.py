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

def nome_valido(texto) -> bool:
    if texto == '':
        return False
    
    for caractere in texto:
        if caractere not in 'AaãáâàBbCcçDdEeêéFfGgHhIiíJjKkLlMmNnOoôõóPpQqRrSsTtUuúVvWwXxYyZz ':
            return False

    return True

if nome_valido(nome):
    if len(nome) <= 4:
        print('Seu nome é curto.')
    elif len(nome) <= 6:
        print('Seu nome é médio.')
    else:
        print('Seu nome é longo')
else:
    print('Digite apenas letras e não deixe espaços em branco.')