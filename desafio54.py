from datetime import date

#Crie um programa que leia o ano de nascimento de 7 pessoas. No final mostre quantas pessoas ainda nao atingiram a maior idade e quantas atingiram, considere a maior idade com 21 anos
ano_atual = date.today().year
maior_idade = 0
menor_idade = 0
for c in range(7):
    nascimento = int(input(f'Pessoa nº {c + 1}, digite seu ano de nascimento: '))
    if ano_atual - nascimento >=21:
        maior_idade += 1
    else:
        menor_idade += 1
print(f'{maior_idade} pessoas são maiores de idade')
print(f'{menor_idade} pessoas são menores de idade')        
    
        
