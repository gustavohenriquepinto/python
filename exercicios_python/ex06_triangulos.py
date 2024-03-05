print('Bem-vindo ao sistema de solução de triângulos!')

calculo = input('Quais informações você possui?\n1 - Três lados.\n2 - Dois lados e um ângulo.\n3 - Um lado e dois ângulos.')[0]
match calculo:
    case 1:
        PONTOS = 'A', 'B', 'C'
        lados = []
        
        for lado in range(3):
            lados.append(input(f'Digite o valor do lado {PONTOS[lado]}: '))