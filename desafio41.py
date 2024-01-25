#A confederação nacional de nataçao precisa de um programa que leia o ano de nascimento de um atleta
# e mostre sua categoria, de acordo com a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JUNIOR
# - Até 20 anos: SÊNIOR
# - Acima: MASTER

idade = int(input('Informe sua idade: '))
if idade <= 9:
    print('CATEGORIA MIRIM')
elif idade <= 14:
    print('CATEGORIA INFANTIL') 
elif idade <= 19:
    print('CATEGORIA JUNIOR')
elif idade == 20:
    print('CATEGORIA SÊNIOR')
else:
    print('CATEGORIA MASTER')               