# Constantes são "variáveis" que não vão mudar

# velocidade_atual = 120
# local_carro = 102

# RADAR_1 = 60
# LOCAL_1 = 100
# RADAR_RANGE = 1

# carro_passou_no_radar: bool = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE)

# if carro_passou_no_radar:
#     print('O carro está passando pelo radar.')

#     if velocidade_atual > RADAR_1:
#         print('O carro foi multado.')
#     else:
#         print('O carro está dirigindo dentro do limite de velocidade.')

# else:
#     print('O carro não passou pelo radar.')

# v1 = 'a'
# v2 = 'a'

# print(id(v1), id(v2))

condicao = False
passou_no_if = None

if condicao:
    passou_no_if = True
    print('Código do IF')
else:
    print('Código do ELSE')

print(passou_no_if, passou_no_if is None)
print(passou_no_if, passou_no_if is not None)