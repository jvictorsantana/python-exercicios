#Faça um programa que leia o ano de nascimento de um jovem, e informe de acordo com a sua idade:
# Se ele ainda vai se alistar no serviço militar
# Se é a hora de se alistar
# Se ja passou do tempo de alistamento
# Seu programa também deve mostrar o tempo que falta ou que passou do prazo..
from datetime import date
nascimento = int(input('Qual o ano do seu nascimento? '))
if 2023 - nascimento == 17:
    print('Você está no ano de alistamento!')
elif 2023 - nascimento > 17:
    print(f'Você já passou {2023 - nascimento - 17} anos da época de alistamento!')    
else:
    print(f'Você ainda nao está na época de alistamento, falta {nascimento  + 17 - 2023} anos pro seu alistamento!')

#Resolução do professor
atual = date.today().year
nasc = int(input('Informe o seu ano de nascimento: '))
idade = atual - nasc
print(f'Quem nasceu em {nasc} tem {idade} anos!')
if idade == 18:
    print('Voce tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print(f'Ainda faltam {saldo} anos para o alistamento')
    ano = atual + saldo
    print(f'Seu alistamento será em {ano}')
elif idade > 18:
    saldo = idade - 18
    print(f'Você já deveria ter se alistado a {saldo} anos')     
    ano = atual - saldo   
    print(f'Seu alistamento foi em {ano}')