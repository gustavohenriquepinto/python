print('Bem-vindo ao calculador de média.')
print('Para calcular a média, digite "M" a qualquer momento.')
print('Você também pode adicionar peso: "8;2" significa que 8 terá peso de 2.')
print('O peso padrão é 1.\n')

soma : float = 0.0
peso : float = 0.0

while True:
    texto_digitado : str = input('Digite o próximo número: ').lower()

    if texto_digitado == 'm' and peso != 0:
        print(f'A média aritmética dos valores é: {soma / peso}')

        if input('Deseja continuar? [S/N]: ').lower().startswith('s'):
            print('')
            soma = 0
            peso = 0
            continue
        else:
            break
    elif texto_digitado == 'm' and peso == 0:
        print('Você inseriu caracteres inválidos.')
        continue

    for caractere in texto_digitado:
        if caractere not in '0123456789+-;,.':
            print('Você inseriu caracteres inválidos.')
            continue

    if ';' not in texto_digitado:
        texto_digitado += ';1'
    
    texto_numero = texto_digitado.split(';', 2)[0]
    texto_peso = texto_digitado.split(';', 2)[1]

    try:
        soma += float(texto_numero) * float(texto_peso)
        peso += float(texto_peso)
    except:
        print('Você inseriu caracteres inválidos.')
        continue
