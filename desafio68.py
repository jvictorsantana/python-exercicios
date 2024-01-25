from random import randint
# Faça um programa que jogue par ou impar com o computador. O jogo so será interrompido quando o jogador perder
# mostrando o total de vitorias consecutivas que ele conquistou no final do jogo

j_cont = 0
c_cont = 0

while True:
    pergunta = ''
    while pergunta != 'p' and pergunta != 'i':
        pergunta = input('Par ou Ímpar [P/I] ').strip().lower()
    jogador = int(input('Digite um número '))
    computador = randint(0,10)
    total = jogador + computador 
    
    if pergunta == 'p' and total % 2 == 0:
        print(f'Você jogou {jogador} e o computador jogou {computador}')
        print(f'-- {total} é PAR')
        print('')
        print(f'-=--=- Jogador ganhou a partida-=--=- ')
        print('')
        j_cont += 1

    elif pergunta == 'i' and total % 2 == 1:
        print('')
        print(f'Você jogou {jogador} e o computador jogou {computador}')
        print(f'-- {total} é ÍMPAR')
        print('')
        print(f'-=--=- Jogador ganhou a partida-=--=- ')
        print('')
        j_cont += 1

    else:
        if total % 2 == 0:
            print('')
            print(f'Você jogou {jogador} e o computador jogou {computador}')
            print(f'-- {total} é PAR')
            print('')
            print(f'-=--=- Computador ganhou a partida-=--=- ')
            print('')

        else:     
            print('')
            print(f'Você jogou {jogador} e o computador jogou {computador}')
            print(f'-- {total} é ÍMPAR')
            print('')
            print(f'-=--=- Computador ganhou a partida-=--=- ')
            print('') 
        break


print('Total da partida')
print('-=-'*8)
print(f'Placar jogador = {j_cont}')    
