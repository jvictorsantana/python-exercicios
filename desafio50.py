#Desenvolva um programa que leia 6 números inteiros e mostre a soma daqueles que for numeros pares apenas.
s = 0
cont = 0
for c in range(1, 7):
    n = int(input(f'Digite o {c}º valor: '))
    if n % 2 == 0:
        s += n
        cont += 1
print(f'Você informou {cont} números pares e a soma foi de {s}')