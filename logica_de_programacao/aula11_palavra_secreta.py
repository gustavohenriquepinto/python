SENHA : str = 'Tesoura'.lower()
senha_formatada : str = ''
letra_digitada : str = ''

for caractere in SENHA:
    senha_formatada += '*'


def atualizar_senha_formatada(letra):
    i = 0
    while i < len(SENHA):
        if SENHA[i] == letra:
            senha_formatada[i] = letra
            i += 1

while True:
    letra_digitada = input('Digite uma letra: ').lower()

    if letra_digitada.isalpha() and len(letra_digitada) == 1:
        
        if letra_digitada in SENHA:
            atualizar_senha_formatada(letra_digitada)
            print('Senha atual:', senha_formatada)
        else:
            print('Senha atual:', senha_formatada)
    else:
        print('Digite apenas uma letra...\n')
        continue

    if SENHA == senha_formatada:
        break

print('Você encontrou a senha!')
    