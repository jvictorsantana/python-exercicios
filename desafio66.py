# Crie um programa que leia varios numeros inteiros pelo teclado. O programa so vai parar quando o usuário digitar
# o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles, desconsiderando o 999
total = 0
contador = 0
while True:
    n = int(input('Digite um número (ou 999 para parar) '))
    if n == 999:
        break
    total += n
    contador += 1 
print(f'A soma dos {contador} números foi {total}')    