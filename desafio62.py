# Melhore o desafio 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando o usuário disser que quer mostrar 0 termos..

print('GERADOR DE PA')
print('-=-'*10)
t1 = int(input('Qual o primeiro termo: '))
razao = int(input('Qual a razão: '))
termo = t1
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print(f'{termo} -> ', end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada!')