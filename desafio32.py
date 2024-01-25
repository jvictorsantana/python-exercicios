#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
ano = int(input('Digite um ano: '))
if ano % 4 == 0 and ano % 400 == 0:
    print('Ano bissexto!')
else:
    print('Não é um ano bissexto!')    