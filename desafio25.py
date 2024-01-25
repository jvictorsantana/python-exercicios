#Crie um programa que leia o nome de uma pessoa e diga se ela tem 'SILVA' no nome. 
nome = input('Digite o seu nome completo: ').strip()
print(nome.upper().find('SILVA'))#Minha resolução me passa o nome indíce da palavra silva, ou seja, onde ela começa.

#resolução do professor
n = input('Digite seu nome completo: ').strip()
print('silva' in n.lower())#Utilizando o 'in' ele me retorna verdadeiro ou falso, podemos combinar a variável com um 'upper' ou 'lower' para que nao haja erros
