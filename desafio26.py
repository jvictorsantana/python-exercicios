#Faça um programa que leia uma frase pelo teclado e mostre:
# - Quantas vezes aparece a letra 'A'
# - Em que posição ela aparece a primeira vez
# - Em que posição ela aparece a última vez. 

frase = input('Digite uma frase: ').strip()
print(f'a letra A aparece {frase.upper().count('A')} vezes')
print(f'a letra A aparece a primeira vez na {frase.upper().find('A')+1}')# +1 porque a contagem do índice começa do zero
print(f'a letra A aparece a última vez na {frase.upper().rfind('A')+1}')#'rfind' - right find - começa a procurar da direita para a esquerda
