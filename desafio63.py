# EScreva um programa que leia um n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequencia de fibonacci

print('SEQUÊNCIA DE FIBONACCI')
print('-'*25)
n = int(input('Quantos termos você quer ver? '))
a = 0
b = 1
cont = 2
while cont <= n:
    print(a, '', b, end= '  ')
    a+=b
    b+=a
    cont+=1
print(' FIM ')

# solução do professor

num = int(input('Quantos termos voce quer ver/ '))
t1 = 0
t2 = 1
print(f'{t1} -> {t2}', end='')
cont = 3
while cont <= num:
    t3 = t1 + t2
    print(f' -> {t3}', end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' -> FIM')