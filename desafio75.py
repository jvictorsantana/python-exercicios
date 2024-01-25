# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A - Quantas vezes aparece o valor 9
# B - Em que posição foi digitado o primeiro valor 3
# C - Quais foram os números pares.

n = int(input('Digite um número ')), int(input('Digite um número ')), int(input('Digite um número ')), int(input('Digite um número '))

print('Os números digitados foram:', end=' ')
for c in n:
    print(f'{c}', end=' ')
print(f'\nO número 9 aparece {n.count(9)} vezes')
if 3 in n:
    print(f'O valor 3 apareceu na {n.index(3)+1}ª posição')
else:
    print('Não contém número 3 nessa lista')

print('Os números pares da lista são:', end=' ')
for u in n:
    if u % 2 == 0:
        print(f'{u}', end=' ')
