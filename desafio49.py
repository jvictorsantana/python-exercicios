#Refaça o exercicio desafio 9 da tabuada mostrando a tabuada de um número que o usuário escolher, so que agora, utilizando um laço for.

n = int(input('Escolha o número para a tabuada: '))
for c in range(1, 11):
    print(f'{n} x {c} = {n*c}')
     