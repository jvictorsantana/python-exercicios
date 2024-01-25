#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsidere os espaços.

n = input(' ').strip().upper().split() #li a frase ou palavra eliminando os espaços e splitando para gerar uma lista
n_junto = ''.join(n) #utilizei o join para juntar essa lista eliminando os espaços internos

inverso = ''
for letra in range(len(n_junto)-1, -1, -1): #fiz o inverso da frase, fui da ultima letra, até a primeira, voltando uma letra
    inverso += n_junto[letra]
print(f'O inverso de {n_junto} é {inverso}')
if inverso == n_junto:
    print('Temos um palíndromo!')

else:
    print('A frase digitada não é um palíndromo!')

'''inverso = n_junto[::-1] -- Esta é uma forma mais simples de fazer o inverso do nome com o fatiamento de string    
 print(inverso)'''


