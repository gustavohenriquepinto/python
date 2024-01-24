 # While executa um código enquanto uma condição for verdadeira.

condicao : int = 0

while condicao <= 100:
    condicao += 1

    if condicao % 3 == 0:
        continue

    print(condicao)

    if condicao == 40:
        break

print('\nSaiu do while.\n')
