#Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas
# - O nome com todas minúsculas
# - Quantas letras ao todo(sem considerar espaços)
# - Quantas letras tem o primeiro nome

n_completo = input('Digite seu nome completo ')
print('Todas as letras em maiúsculo', n_completo.upper())
print('Todas as letras em minúsculos', n_completo.lower())
print('A quantidade de caracteres sem espaços é:', len(''.join(n_completo.split())))#Fiz de dentro para fora, utilizei o split para quebrar  
#o nome em listas, o join para juntar sem espaço e o len para contar a quantidade

print('A quantidade das letras do primeiro nome é: ', len(n_completo.split()[0]))#Utilizei o split para quebrar em listas, usei o zero em colchetes
# para trazer a primeira lista, que no caso foi o primeiro nome, e o len para contar a quantidade de caracteres


#Resolução do Professor

nome = str(input('Digite seu nome completo ')).strip() #strip para tirar os espaços indesejados que pode ter no começo e no final

#vou digitar apenas as ultimas duas situações que foram mais complexas e, embora dê o mesmo resultado que o meu, foram feitas de forma diferentes
print(len(nome) - nome.count(' ')) #Ele utiliza len para contar a quantidade de caracteres e subtrai utilizando count para contar a quantidade de espaços
print(nome.find(' '))#Ele utiliza find para encontrar o primeiro espaço após o primeiro nome, trazendo assim o índice da quantidade de caracteres do nome
