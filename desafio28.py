#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
# peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
#O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep
print('-=-'*20)
print('Vou pensar em um número de 0 a 5, tente adivinhar')
print('-=-'*20)
computador = randint(0,5)
sleep(2)
palpite = int(input('Digite um número de 0 a 5: '))
if palpite == computador:
    sleep(2)
    print('PROCESSANDO ...')
    sleep(2)
    print(f'Parabéns, o número foi o {computador}, você acertou!')
else:
    sleep(2)
    print('PROCESSANDO ...')
    sleep(2)
    print(f'Resposta errada, o número correto foi o {computador}!')

    #RESOLUÇÃO PROFESSOR
    #
        
