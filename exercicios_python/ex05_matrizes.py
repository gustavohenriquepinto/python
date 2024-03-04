#region Encontrar maior elemento

# maior_elemento = 0

# for linha in range(linhasA):    
#     for coluna in range(colunasA):
#         if matrizA[linha][coluna] > maior_elemento:
#             maior_elemento = matrizA[linha][coluna]

# print(maior_elemento)

#endregion

#region Matriz Identidade
# matrizI = []
# ordemI = int(input('Ordem da Matriz Identidade: '))

# for linha in range(ordemI):
#     matrizI.append([])

#     for coluna in range(ordemI):
#         matrizI[linha].append(1 if linha == coluna else 0)

#         print(f'[{matrizI[linha][coluna]}]', end= '\n' if coluna == ordemI -1 else ' ')
#endregion

#region Matriz com valores de outras duas
# matrizA, matrizB = [], []

# print('Defina a matriz A: ')
# linhasA = int(input('Número de linhas: '))
# colunasA = int(input('Número de colunas: '))

# for linha in range(linhasA):
#     matrizA.append([])
#     for coluna in range(colunasA):
#         matrizA[linha].append(float(input(f'Digite o valor de A[{linha + 1},{coluna + 1}]: ')))

# print('\nDefina a matriz B: ')

# for linha in range(linhasA):
#     matrizB.append([])
#     for coluna in range(colunasA):
#         matrizB[linha].append(float(input(f'Digite o valor de B[{linha + 1},{coluna + 1}]: ')))

        

# for linha in range(linhasA):
#     for coluna in range(colunasA):

#         if matrizA[linha][coluna] > matrizB[linha][coluna]:
#             print(f'[{matrizA[linha][coluna]}]', end= '\n' if coluna == linhasA -1 else ' ')
#         else:
#             print(f'[{matrizB[linha][coluna]}]', end= '\n' if coluna == linhasA -1 else ' ')

#endregion

#region Jogo da Velha
tabuleiro = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

vencedor = 0
turno = 1

while vencedor == 0:
    coordenada_usuario = input(f'Vez do Jogador {turno}: ').split(',')
    eixo_x = int(coordenada_usuario[0]) - 1
    eixo_y = int(coordenada_usuario[1]) - 1


    if tabuleiro[eixo_x][eixo_y] != 0:
        print('Esse espaço já está ocupado!')
        continue

    tabuleiro[eixo_x][eixo_y] = turno

    casa_vazia, casa_cheia = False, False
    for linha in range(3):
        for coluna in range(3):
            coordenada = tabuleiro[linha][coluna]
            marcador = ' ' if coordenada == 0 else 'x' if coordenada == 1 else 'o'

            print(f'[{marcador}]', end= '\n' if coluna == 2 else ' ')

            if coordenada == 0:
                casa_vazia = True
            else:
                casa_cheia = True
    
    if casa_cheia and not casa_vazia:
        vencedor = -1
    
    for linha in range(3):
        if tabuleiro[linha][0] == tabuleiro[linha][1] == tabuleiro[linha][2] != 0:
            vencedor = turno

    for coluna in range(3):
        if tabuleiro[0][coluna] == tabuleiro[1][coluna] == tabuleiro[2][coluna] != 0:
            vencedor = turno

    turno = 1 if turno == 2 else 2

if vencedor == -1:
    print('Temos um empate!')
else:
    print(f'O Jogador {vencedor} ganha a partida!')