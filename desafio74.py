# Crie um programa que vai gerar 5 números aleatórios e colocar em uma tupla. 
# Depois disso, mostre a listagem dos números gerados e indique o menor e o maior valor que estão na tupla.

from random import randint

n = randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10)
print('Os números na lista são')
for c in n:
    print(f'{c}', end=' ')
print(f'\nO maior número sorteado foi o {max(n)}\nO menor número sorteado foi o {min(n)}')