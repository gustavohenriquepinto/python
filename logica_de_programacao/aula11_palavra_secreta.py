senha = 'perfume'
letras_acertadas = ''

while True:
    letra_digitada = input('Digite uma letra: ')

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue

    if letra_digitada in senha:
        letras_acertadas += letra_digitada

    print('Senha: ', end='')
    for letra in senha:
        print(f'{letra if letra in letras_acertadas else '*'}', end='')
    print('')

