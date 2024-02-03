print('Bem-vindo ao sistema de cálculo de bases numéricas.')

algarismos = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def NumeroValido(numero : str, base : int) -> bool:
    for caractere in numero:
        if caractere not in algarismos[0:base]:
            return False
    
    return True

def ConverterParaBase10(numero : str, base : int) -> int:
    if base == 10 and numero.isdigit():
        return int(numero)
    
    soma_caracteres = 0
    for indice, caractere in enumerate(numero):
        soma_caracteres += algarismos.index(caractere) * base ** (len(numero) - 1  - indice)

    return soma_caracteres

def ConverterDaBase10(numero : int, base : int) -> str:
    if base == 10 and numero.isdigit():
        return str(numero)
    
    texto_invertido = ''
    while numero >= base:
        texto_invertido += algarismos[numero % base]
        numero //= base
    texto_invertido += algarismos[numero]

    return texto_invertido[::-1]

def Calcular(num1 : int, calculo : str, num2 : int) -> int:
    match calculo:
        case '+':
            return num1 + num2
        case '-':
            return num1 + num2
        case '*':
            return num1 * num2
        case '/':
            return num1 // num2
        case '%':
            return num1 % num2
        case '^':
            return num1 ** num2
        case _:
            return 0
    
while True:
    operacao = input('O deseja fazer agora?\n1 - Converter de uma base para outra.\n2 - Realizar cálculos com qualquer base.\n3 - Encerrar.\nDigite: ')[0]

    match operacao:
        case '1':

            base_atual = input('\nDigite a base do número para converter: ')
            if not (base_atual.isdigit() and int(base_atual) > 1 and int(base_atual) < 37):
                print('Digite um número inteiro entre 2 e 36.\n')
                continue
            base_atual = int(base_atual)

            numero_atual = input('Digite o número para converter: ').upper()        
            if not NumeroValido(numero_atual, base_atual):
                print('Você digitou algum algarismo inválido.\n')
                continue

            nova_base = input('Digite a base desejada: ')
            if not (nova_base.isdigit() and int(nova_base) > 1 and int(nova_base) < 37):
                print('Digite um número inteiro entre 2 e 36.\n')
                continue
            nova_base = int(nova_base)

            print(f'\nResultado: {ConverterDaBase10(ConverterParaBase10(numero_atual, base_atual), nova_base)}, na base {nova_base}.\n')
            
        case '2':

            primeira_base = input('\nDigite a base do primeiro número: ')
            if not (primeira_base.isdigit() and int(primeira_base) > 1 and int(primeira_base) < 37):
                print('Digite um número inteiro entre 2 e 36.\n')
                continue
            primeira_base = int(primeira_base)

            primeiro_numero = input('Digite o primeiro número: ').upper()        
            if not NumeroValido(primeiro_numero, primeira_base):
                print('Você digitou algum algarismo inválido.\n')
                continue

            calculo = input("Escolha uma operação:\n\'+' - Soma\n'-' - Subtração\n'*' - Multiplicação\n'/' - Divisão inteira\n'%' - Resto da divisão\n'^' - Exponenciação\nDigite: ")[0]

            if calculo not in '+-*/%^~':
                print('Você digitou uma operação inválida.\n')
                continue
            
            segunda_base = input('\nDigite a base do segundo número: ')
            if not (segunda_base.isdigit() and int(segunda_base) > 1 and int(segunda_base) < 37):
                print('Digite um número inteiro entre 2 e 36.\n')
                continue
            segunda_base = int(segunda_base)

            segundo_numero = input('Digite o segundo número: ').upper()        
            if not NumeroValido(segundo_numero, segunda_base):
                print('Você digitou algum algarismo inválido.\n')
                continue

            base_retorno = input('Digite a base de retorno: ')
            if not (base_retorno.isdigit() and int(base_retorno) > 1 and int(base_retorno) < 37):
                print('Digite um número inteiro entre 2 e 36.\n')
                continue
            base_retorno = int(base_retorno)

            print(f'Resultado: {ConverterDaBase10(Calcular(ConverterParaBase10(primeiro_numero, primeira_base), calculo, ConverterParaBase10(segundo_numero, segunda_base)), base_retorno)}')

        case '3':
            break

        case _:
            print('Operação inexistente!\n')
            continue

