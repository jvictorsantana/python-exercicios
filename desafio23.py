#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
#EX: Digite um numero:1834
# - unidade: 4
# - dezena: 3
# - centena: 8
# - milhar: 1

n = int(input('Digite um numero de 0 a 9999 '))

#print(' '.join(n).split())
print(f'unidade: {n // 1 % 10}\ndezena: {n // 10 % 10}\ncentena: {n//100%10}\nmilhar: {n//1000%10}')