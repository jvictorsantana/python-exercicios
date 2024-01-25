#Crie um programa que faça o computador jogar jokenpo com você
from time import sleep
from random import choice
p_computador = 0
p_jogador = 0 
while p_computador < 10 or p_jogador <10:
    
    print('-=-'*20)
    print(f'Jogador: {p_jogador}\nComputador: {p_computador}')
    print('-=-'*20)
      
    computador = ['pedra', 'papel', 'tesoura']
    jogador = input('-=- Escolha sua jogada -=-\n1) Pedra\n2) Papel\n3) Tesoura\n -- ').strip().lower()
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO')
    jogada_computador = choice(computador)

    if jogador == 'pedra' and jogada_computador == 'tesoura':
        print('-=-'*5)
        print(f'VOCÊ JOGOU {jogador}')
        print(f'Computador jogou {jogada_computador}')
        print('-=-'*5)
        print('Você ganhou a rodada!')
        p_jogador+=1
    elif jogador == 'papel' and jogada_computador == 'pedra':
        print('-=-'*5)
        print(f'VOCÊ JOGOU {jogador}')
        print(f'Computador jogou {jogada_computador}')
        print('-=-'*5)
        print('Você ganhou a rodada!')
        p_jogador+=1
    elif jogador == 'tesoura' and jogada_computador == 'papel':
        print('-=-'*5)
        print(f'VOCÊ JOGOU {jogador}')
        print(f'Computador jogou {jogada_computador}')
        print('-=-'*5)
        print('Você ganhou a rodada!')
        p_jogador+=1
    elif jogada_computador == 'pedra' and jogador == 'tesoura':
        print('-=-'*5)
        print(f'VOCÊ JOGOU {jogador}')
        print(f'Computador jogou {jogada_computador}')
        print('-=-'*5)
        print('COMPUTADOR ganhou a rodada!')
        p_computador+=1
    elif jogada_computador == 'papel' and jogador == 'pedra':
        print('-=-'*5)
        print(f'VOCÊ JOGOU {jogador}')
        print(f'Computador jogou {jogada_computador}')
        print('-=-'*5)
        print('COMPUTADOR ganhou a rodada!')
        p_computador+=1
    elif jogada_computador == 'tesoura' and jogador == 'tesoura':
        print('-=-'*5)
        print(f'VOCÊ JOGOU {jogador}')
        print(f'Computador jogou {jogada_computador}')
        print('-=-'*5)
        print('COMPUTADOR ganhou a rodada!')
        p_computador+=1
    else:
        print('-=-'*5)
        print(f'VOCÊ JOGOU {jogador}')
        print(f'Computador jogou {jogada_computador}')
        print('-=-'*5)
        print('Deu Empate')    
      
print('Jogo Finalizado!')        



