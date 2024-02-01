print('\nBem-vindo à calculadora de Fibonacci.')

fibonacci = []

try:
    quantidade = int(input('Quantos números da sequência de fibonacci deseja obter?'))
except:
    print('Digite um número natural não nulo.')

for indice in quantidade:
    fibonacci.insert(indice - 1, 1 if indice <= 2 else fibonacci[indice - 1] + fibonacci[indice - 2])

print('Sequência: ', fibonacci)    

