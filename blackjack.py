import random
from time import sleep

print('-=-'*5,'SEJA BEM VINDO AO CASSINO PORTO SEGURO','-=-'*5)
sleep(1.3)
print('Você está preparado para jogar o maior jogo de cartas de todos os tempos?')
sleep(1.5)
print('-=-'*9,'BLACKJAAAAAACK','-=-'*9)
sleep(1.5)
#deck de cartas do jogador e dealer, começa vazio
deck_jogador = []
deck_dealer = []
#baralho do jogo
dealer = [1,2,3,4,5,6,7,8,9,10,10,10,10,11]
nome = input('Informe o seu nome: ').strip().title()

#escolhendo duas cartas para o dealer
deck_dealer.append(random.choice(dealer))
dealer.remove(deck_dealer[0])
deck_dealer.append(random.choice(dealer))
dealer.remove(deck_dealer[1])

#escolhendo duas cartas para o jogador
deck_jogador.append(random.choice(dealer))
dealer.remove(deck_jogador[0])
deck_jogador.append(random.choice(dealer))
dealer.remove(deck_jogador[1])

#Mostra as cartas do dealer, sendo uma virada para baixo e uma amostra
print('-=-'*20)
print(f'-- Deck Dealer:\nDealer tem uma carta virada X e sua outra carta é {deck_dealer[1]}')
print('-=-'*20)

#Mostra as duas primeiras cartas do jogador
print('-=-'*20)
print(f'Deck {nome}: {deck_jogador}\n{sum(deck_jogador)}')
print('-=-'*20)

# Verificar se o jogador ou Dealer já tem 21 pontos
if sum(deck_jogador) == 21:
    print(f'Parabéns, {nome}! Você obteve Blackjack! Você venceu a partida!')
    exit()
elif sum(deck_dealer) == 21:
    print(f'Dealer obteve Blackjack! Você perdeu a partida!')
    exit()

#jogada do jogador enquanto nao tem 21 pontos
while sum(deck_jogador) <21:
  random.shuffle(dealer) #embaralha o as cartas
  jogo = int(input('Solicite suas cartas\n(1) Hit\n(2) Stand\n -- '))
  if jogo == 1:
    print('Embaralhando as cartas')
    print('aguarde ... ...')
    sleep(1.5)
    print('escolhendo a carta')
    sleep(1.5)
    embaralhar = random.choice(dealer) #escolhe uma carta do baralho
    dealer.remove(embaralhar) #remove do baralho a carta escolhida
    deck_jogador.append(embaralhar) #adciona no deck do jogador a carta escolhida
    sleep(1.5)
    print('-=-'*20)
    print(f'Deck {nome}: {deck_jogador}\n{sum(deck_jogador)}')
    print('-=-'*20)
    sleep(1.5)
  elif jogo != 2:
      print()
      print('Opção incorreta, informe uma opção válida!')
      print()
  else:
    break

if sum(deck_jogador) > 21: #verifica se o jogador estourou sua pontuação, se passar dos 21 o dealer ganha automaticamente
    print('-=-'*5, f'{nome} estourou a pontuação. Dealer Venceu a Partida!', '-=-'*5)
    exit()
elif sum(deck_jogador) == 21: #verifica se o jogador conseguiu fazer 21 pontos, se conseguiu, jogador ganha automaticamente
    print(f'-=-'*5, f'{nome} Venceu a Partida!', '-=-'*5)
    exit()
else:
    print('Vez do Dealer!')#se jogador nao alcançou os objetivos acima, Dealer joga

    while sum(deck_dealer) <17:
        print('Embaralhando as cartas')
        print('aguarde ... ...')
        sleep(1.3)
        random.shuffle(dealer)
        print('escolhendo a carta')
        sleep(1.3)
        embaralhar = random.choice(dealer)
        dealer.remove(embaralhar)
        deck_dealer.append(embaralhar)
        sleep(1.3)
        print('-=-'*20)
        print(f'{dealer}\n{deck_dealer}\n{sum(deck_dealer)}')
        print('-=-'*20)

    # Condições para funcionamento das partidas

    #se o jogador fizer 21 pontos e o delaer passar ou fizer menos, jogador ganha
    if sum(deck_jogador) == 21 or (sum(deck_dealer) > 21 and sum(deck_jogador) <= 21):
        print('-=-'*5, f'{nome} Venceu a Partida!', '-=-'*5)
    #se jogador e dealer finalizarem a rodada com o mesmo numero de pontos abaixo de 21, jogo empata
    elif sum(deck_dealer) == sum(deck_jogador):
        print('Empate, ninguém ganhou!')
    else:
        #se a soma do deck de quaisquer for maior que a do outro, mesmo sem alcançar 21 pontos, a maior pontuação ganha
        vencedor = nome if sum(deck_jogador) > sum(deck_dealer) else 'Dealer'
        print(f'-=-'*5, f'{vencedor} Venceu a Partida!', '-=-'*5)
