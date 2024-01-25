# Refaça o desafio 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

print('GERADOR DE PA')
print('-=-'*10)
t1 = int(input('Qual o primeiro termo: '))
razao = int(input('Qual a razão: '))
termo = t1
cont = 1
while cont <= 10:
    print(f'{termo} -> ', end='')
    termo += razao
    cont += 1
print('FIM')

