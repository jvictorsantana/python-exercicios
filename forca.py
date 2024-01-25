import random
from time import sleep

print('SEJA BEM VINDO AO JOGO DA FORCA')
print()
lista_palavras = ('banana', 'cenoura', 'laranja', 'paralelepipedo', 'porta', 'santos')
palavra = random.choice(lista_palavras).lower()
tentativa = 0
advinhar = ['_'] * len(palavra)

while '_' in advinhar:
    print(f"A palavra contém {len(palavra)} letras, você tem 6 chances")
    tentativa_jogador = input('Escolha uma letra: ').lower()


    if tentativa_jogador in palavra:
        indices = [i for i, letra in enumerate(palavra) if letra == tentativa_jogador]

        for indice in indices:
            advinhar[indice] = tentativa_jogador
    else:
        tentativa += 1

    print(f"Letra escolhida: {tentativa_jogador}\n{' '.join(advinhar).upper()}")

    if ''.join(advinhar) == palavra:
         print('Você conseguiu!')
         break

    if tentativa == 6:
        print('Você atingiu o número máximo de tentativas. A palavra era:', palavra)
        break




