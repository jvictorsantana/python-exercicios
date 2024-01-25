# Melhore o jogo do desafio 28, onde o computador vai 'pensar' em um número de 0 a 10. Só que agora o jogador vai tentar adivinhar ate acertar, mostrando no final quantos palpites foram necessarios para vencer.

from random import randint

computador = randint(1,10)
palpite = 0
chute = 0
while palpite != computador:
    jogador = int(input('Digite um número: '))
    palpite = jogador
    chute += 1
    
    if palpite == computador:
        print(f'Parabéns, você conseguiu!\nO computador também pensou no {computador}')
        print(f'Você precisou de {chute} chutes para acertar')
    else:
        print(f'Você não acertou, tente novamente!') 
        print(f'{chute}º Chute')   
   


