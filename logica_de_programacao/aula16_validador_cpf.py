
import re
import random

numero_cpfs = 10
while numero_cpfs > 0:
    texto_numero = ''
    
    # texto_usuario = re.sub(
    #     r'[^0-9]',
    #     '',
    #     input('Digite  os nove primeiros números do seu CPF: '),
    # )

    # if (not texto_usuario.isnumeric()) or int(texto_usuario) < 100000000:
    #     if texto_usuario.upper().startswith('S'):
    #         print('Tchau!')
    #         break

    #     print('Digite apenas os nove primeiros números!')
    #     continue
    # else:
    #     texto_numero = texto_usuario
    
    for i in range(9):
        texto_numero += str(random.randint(0, 9))
    

    contador_regressivo = 10
    soma_digitos = 0
    for digito in texto_numero:
        soma_digitos += int(digito) * contador_regressivo
        contador_regressivo -= 1

    validador_1 = (soma_digitos * 10) % 11
    validador_1 = validador_1 if validador_1 < 10 else 0

    contador_regressivo = 11
    soma_digitos = 0
    for digito in texto_numero + str(validador_1):
        soma_digitos += int(digito) * contador_regressivo
        contador_regressivo -= 1
    
    validador_2 = (soma_digitos * 10) % 11
    validador_2 = validador_2 if validador_2 < 10 else 0

    # print(f'Os dígitos validadores são {validador_1}{validador_2}.')

    print(texto_numero + str(validador_1) + str(validador_2))
    numero_cpfs -= 1



