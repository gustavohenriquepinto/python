print('Bem-vindo ao sistema de conversão de algarismos romanos.')

algarismosRomanos = {1 : 'I', 5 : 'V', 10 : 'X', 50 : 'L', 100 : 'C', 500 : 'D', 1000 : 'M'}

caracteres_perimitidos = '0123456789IVXLCDM'

def NumeroValido (numero : str) -> list:
    for caractere in numero:
        if caractere not in caracteres_perimitidos:
            return [False, 0]

    if texto_usuario.isdigit() and 0 < int(numero) < 4000:
        return [True, int(numero)]
    elif texto_usuario.isdigit():
        return [False, 0]
    
    else:
        if EstaDentroDe(numero, ['IIII', 'VV', 'XXXX', 'LL', 'CCCC', 'DD', 'MMMM']):
            return [False, 0]
        elif EstaDentroDe(numero, ['IM', 'VM', 'XM', 'LM', 'CCM', 'DM']):
            return [False, 0]
        elif EstaDentroDe(numero, ['ID', 'VD', 'XD', 'LD', 'CCD']):
            return [False, 0]
        elif EstaDentroDe(numero, ['IC', 'VC', 'XXC', 'LC']):
            return [False, 0]
        elif EstaDentroDe(numero, ['IL', 'VL', 'XXL']):
            return [False, 0]
        elif EstaDentroDe(numero, ['IIX', 'VX', 'IIV']):
            return [False, 0]
    
    return [True, numero]

        
def EstaDentroDe(texto : str, substrings : list) -> bool:
    for item in substrings:
        if item in texto:
            return True
    return False

def IndoarabicosParaRomanos(numero : int) -> str:
    numero = str(numero)
    retorno = ''

    for indice, caractere in enumerate(numero):
        caractere = int(caractere)

        if caractere == 9 or caractere == 4:
            retorno += algarismosRomanos[10 ** (len(numero) - indice - 1)] + algarismosRomanos[5 if caractere == 4 else 10 * 10 ** (len(numero) - indice - 1)]
        elif caractere < 5:
            retorno += caractere * algarismosRomanos[10 ** (len(numero) - indice - 1)]
        elif caractere < 9:
            retorno += algarismosRomanos[5 * 10 ** (len(numero) - indice - 1)] + (caractere - 5) * algarismosRomanos[10 ** (len(numero) - indice - 1)]
        else:
            print('Ocorreu um erro inesperado...')
    
    return retorno

def RomanosParaIndoarabicos(numero : str) -> int:
    ...

    
while True:
    texto_usuario = input('\nDigite o número para converter ou S para sair: ').upper()

    validacao = NumeroValido(texto_usuario)
    if validacao[0]:
        if type(validacao[1]) == int:
            print(IndoarabicosParaRomanos(validacao[1]))
        elif type(validacao[1]) == str:
            print(RomanosParaIndoarabicos(validacao[1]))
        else:
            print('Ocorreu um erro inesperado...')

    elif texto_usuario.startswith('S'):
        break

    else:
        print('Você não digitou um número válido!\nDigite um número em algarismos romanos ou indoarábicos inteiros entre 1 e 3999.')