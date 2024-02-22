string = 'ABCD'
lista = ['Olá, mundo!', -1, 0.3, True]
tupla = 'Tchau, mundo!', 1, -0.3, False

a, b, *_, c = lista

# print(a, c)

print(tupla)
print(*tupla)

print(string)
print(*string)