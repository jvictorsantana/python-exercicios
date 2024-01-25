import random

def player():
        jogada = input('Escolha Pedra, Papel ou Tesoura:  ')
        return jogada

def computador():
        jogada_c = ['pedra', 'papel', 'tesoura']

        return random.choice(jogada_c)

def jogo(player, computador):

        if player == 'pedra' and computador == 'tesoura':
            print(f'{jogador} VENCEU A RODADA!')
            return 1
        elif player == 'tesoura' and computador == 'papel':
            print(f'{jogador} VENCEU A RODADA!')
            return 1
        elif player == 'papel' and computador == 'pedra':
            print(f'{jogador} VENCEU A RODADA!')
            return 1
        if computador == 'pedra' and player == 'tesoura':
            print('Computador VENCEU A RODADA!')
            return -1
        elif computador == 'tesoura' and player == 'papel':
            print('Computador VENCEU A RODADA!')
            return -1
        elif computador == 'papel' and player == 'pedra':
            print('Computador VENCEU A RODADA!')
            return -1
        else:
            print('empate, jogue novamente')
            return 0
        
