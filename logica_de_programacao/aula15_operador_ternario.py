while True:
    num1, num2 = None, None

    try:
        num1 = float(input('Digite um número: '))
        num2 = float(input('Digite outro número: '))
    except:
        print('Por favor, digite apenas números!')
        break

    print(f'{f'{num1} é maior que {num2}.' if num1 > num2 else f'{num1} é menor que {num2}.' if num1 < num2 else f'{num1} e {num2} são iguais.'}')
