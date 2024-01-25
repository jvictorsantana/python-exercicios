#Faça um programa que calcule a soma de todos os numeros impares que sao multiplos de 3 e que se encontram no intervalo de 1 e 500
s = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        s += c
print(s)
