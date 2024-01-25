# Crie um programa que leia varios numeros inteiros pelo teclado. no final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuario se ele quer ou nao continuar a digitar

p = input('Deseja digitar algum número? [S/N] ').upper()
soma = 0
quantidade = 0
maior = 0
while p != 'N':
    num = int(input('Digite o número '))
    soma += num
    quantidade += 1
    if num > maior:
        maior = num
    p = input('Deseja digitar algum número? [S/N] ').upper()
    
media = soma / quantidade
print(f'\nVocê digitou {quantidade} números\nO maior número é {maior}\nA soma de todos os números é {soma}\nA média dos números digitados é de {media:.2f}\n')
