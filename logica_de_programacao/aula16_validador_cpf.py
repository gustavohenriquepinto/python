
# 754.233.956-74
# 754233956

# 70+45+32+14+18+15+36+15+12 = 257
# 257 * 10 = 2570
# 2570 % 11 = 7


while True:
    texto_usuario = input('Digite  os nove primeiros números do seu CPF: ')

    if not texto_usuario.isnumeric():
        if texto_usuario.upper().startswith('S'):
            print('Tchau!')
            break

        print('Digite apenas números!')
        continue

    contador_regressivo = 10
    soma_digitos = 0
    for digito in texto_usuario:
        soma_digitos += int(digito) * contador_regressivo
        contador_regressivo -= 1

    validador_1 = (soma_digitos * 10) % 11
    validador_1 = validador_1 if validador_1 < 10 else 0

    contador_regressivo = 11
    soma_digitos = 0
    for digito in texto_usuario + str(validador_1):
        soma_digitos += int(digito) * contador_regressivo
        contador_regressivo -= 1
    
    validador_2 = (soma_digitos * 10) % 11
    validador_2 = validador_2 if validador_2 < 10 else 0

    print(f'Os dígitos validadores são {validador_1}{validador_2}.')
