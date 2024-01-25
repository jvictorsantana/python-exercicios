#Faça um programa que leia um numero inteiro e diga se ele é ou não um número primo. (numeros divisiveis por 1 e por ele mesmo)
n = int(input(' '))
total = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[34m', end='')
        total += 1
    else:
        print('\033[31m', end='') 
    print(c, end=' ')
print(f'\n\033[m0 Número {c} foi dividido {total} vezes')
if total == 2:
    print('Número é primo')
else:
    print('Não é primo')        