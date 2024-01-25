#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'SANTO'
cidade = input('digite o nome da cidade: ').strip()
print('santo' in cidade)

#resolução do professor
c = input('Digite o nome da cidade: ').strip() #utiliza o strip para elimiar os espaços caso o usuário aperte antes de escrever
print(c[:5].upper() == 'SANTO') #diferente do que eu fiz, essa resolução do professor foi colocado um upper para fazer a confirmação caso o usuário escreva em letras maiusculas e minusculas
#Ao inves dele utilizar o 'in', ele utilizou o colchetes com a quantidade de caracteres da palavra pedida, dessa forma fica mais simples combinar com outros métodos e chegar no resultado almejado.
