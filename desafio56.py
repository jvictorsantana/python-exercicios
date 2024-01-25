#DEsenvolva um programa que leia nome, idade e sexo de 4 pessoas. No final o programa deve mostrar:
#A média de idade das pessoas do grupo
#Qual o nome do homem mais velho
#Quantas mulheres tem menos de 21 anos


soma_idade = 0
media_idade = 0
maioridadehomem = 0
idademulher = 0
nome_maisvelho = ''
for c in range(1,5):
    print('-=-'*5,f'PESSOA {c}','-=-'*5)
    nome = input('Nome: ').strip()
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').strip().upper()
    soma_idade+=idade
    if c == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nome_maisvelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nome_maisvelho = nome    
    if  sexo in 'Ff' and idade < 20:
        idademulher += 1
media_idade = soma_idade /4   
print(f'A média de idade das pessoas do grupo é de {media_idade}') 
print(f'O homem mais velho tem {maioridadehomem} anos e se chama {nome_maisvelho.title()}')
print(f'{idademulher} mulheres tem menos de 21 anos')

