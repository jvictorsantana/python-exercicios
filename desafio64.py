# Crie um programa que leia varios numeros inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o 999)

n = int(input('Digite um número: '))
total = 0
cont = 0
while n != 999:
        total += n
        cont += 1
        print(f'SOMA: {total}\n')
        print(f'QUANTIDADE {cont}\n')
        n = int(input('Digite um número: '))
print(f'O total da soma foi {total}')