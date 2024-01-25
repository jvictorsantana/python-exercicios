# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores de 'M' ou 'F'. 
# Caso esteja errado, peça a digitaçao novamente até ter o valor correto

sexo = ''
while sexo == '': 
    genero = input('Qual o seu sexo [M/F]: ')
    if genero == 'm':
        sexo += 'm'
    elif genero == 'f':
        sexo += 'f'    
    else: 
        print()
        print('Digite um genero válido!')    
        print()
if sexo == 'm':
    print(f'Seu gênero é masculino')
else:
    print(f'Seu gênero é feminino')
         
    
