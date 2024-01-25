import random
from time import *

def jogar_dado():
    return random.randint(1, 6)

def aplicar_regras(casas, pontos, jogador, dado):
    regras = {
        (2): 1,
        (3): 2,
        (5): 3,
        (6): 'Coringa de Multiplicação',
        (7): 2,
        (13): 2,
        (15): 'Coringa de Subtração',
        (22): 3,
        (31): 'Coringa de Subtração',
        (38): 3,
        (10): 5,
        (18): 5,
        (16): 7,
        (29): 8,
        (41): 'Coringa da Divisão',
        (36): 8,
        (42): 8,
        (27): 9,
        (37): 9,
        (44): 10,
        (8): 1,
        (24): 'Coringa de Subtração',
        (21): 4,
        (28): 3,
        (33): 'Coringa da Divisão',
        (11): 'Coringa de Multiplicação',
        (20): 4,
        (26): 5,
        (4): 5,
        (32): 1,
        (23): 'Coringa de Subtração',
        (12): 10,
        (19): 'Coringa de Subtração',
        (39): 12
    }

    if casas in regras:
        if isinstance(regras[casas], int):
            pontos += regras[casas]
            sleep(2)
            print(f'{jogador} Você ganhou {regras[casas]} pontos')
            print()
            sleep(2)
            print(f'{jogador}: {pontos} pontos')
        elif regras[casas] == 'Coringa de Multiplicação':
            pontos *= 2
            sleep(2)
            print(f'{jogador} Você caiu no Coringa da multiplicação, dobre sua pontuação!')
            sleep(2)
            print(f'{jogador} Você ganhou {pontos} pontos')
            print()
            sleep(2)
            print(f'{jogador}: {pontos} pontos')
        elif regras[casas] == 'Coringa de Subtração':
            pontos -= 5
            sleep(2)
            print(f'{jogador} Você caiu no Coringa de Subtração, perdeu 5 PONTOS!')
            sleep(2)
            print(f'{jogador} Você perdeu 5 pontos')
            sleep(2)
            print()
            print(f'{jogador}: {pontos} pontos')
        elif regras[casas] == 'Coringa da Divisão':
            pontos //= 2
            sleep(2)
            print(f'{jogador} Você caiu no Coringa da Divisão, você perdeu a METADE DOS SEUS PONTOS!')
            sleep(2)
            print(f'{jogador} Você perdeu {pontos} pontos')
            sleep(2)
            print()
            print(f'{jogador}: {pontos} pontos')
        # Adicione mais casos para os coringas aqui...


    else:
        sleep(2)
        print(f'{jogador} Você não ganhou pontos nesta rodada!')
        sleep(2)
        print(f'{jogador}, você tem {pontos} pontos')
        sleep(2)
        print(f'{jogador}: {pontos} pontos')

    return pontos

def jogada_jogador(jogador):
    print()
    print(f'Jogada do {jogador}')
    sleep(2)
    print('*'*60)
    print('1 - JOGAR DADO')
    print('2 - ENCERRAR JOGADA!')
    print('*'*60)
    escolha = int(input())
    print()
    print('rolando os dados')
    sleep(2)
    print('Checando os dados ... ... ')
    sleep(2)

    if escolha == 1:
        return jogar_dado()
    else:
        print(f'Jogada do {jogador} encerrada.')
        return 0  # Se a jogada for encerrada, o dado é 0

def iniciar_jogo():
    vitoria_jogador = 0
    vitoria_computador = 0
    casa_jogador = 0
    casa_computador = 0
    pontos_jogador = 0
    pontos_computador = 0

    jogador = input('Digite seu nome: ')

    while pontos_jogador < 100 and pontos_computador < 100:
        # Jogada do jogador humano
        dado_jogador = jogada_jogador(jogador)
        casa_jogador = (casa_jogador + dado_jogador) % 44
        if casa_jogador == 0:
            casa_jogador = 44
        print()
        print(f'Ande {dado_jogador} casas')
        print(f'{jogador} está na casa {casa_jogador}')
        pontos_jogador = aplicar_regras(casa_jogador, pontos_jogador, jogador, dado_jogador)

        # Jogada do jogador computador (automático)
        dado_computador = jogar_dado()
        casa_computador = (casa_computador + dado_computador) % 44
        if casa_computador == 0:
            casa_computador = 44
        print()
        print(f'Ande {dado_computador} casas')
        print(f'Computador está na casa {casa_computador}')
        pontos_computador = aplicar_regras(casa_computador, pontos_computador, 'Computador', dado_computador)

        print()
        print('*'*15,'Pontuação da rodada:', '*'*15)
        print(f'{jogador}: {pontos_jogador} \nComputador: {pontos_computador}')


        if pontos_jogador >= 100:
          vitoria_jogador += 1

          print()
          print('*************'f'Vitória do {jogador}''*************')
        elif pontos_computador >= 100:
          vitoria_computador += 1

          print()
          print('*'*30, 'Vitória do Computador', '*'*30)


if __name__ == "__main__":
    iniciar_jogo()
