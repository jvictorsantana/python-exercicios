# Crie uma tupla com os 20 primeiros colocados na tabela do Brasileirão, na ordem de colocação. Depois mostre:
# A - Apenas os 5 primeiros colocados
# B - Os Últimos 4 colocados da tabela
# C - Uma lista com os times em ordem alfabética. 
# D - Em que posição na tabela está o time do Santos

brasileirao = ('flamengo', 'santos', 'palmeiras', 'gremio', 'athletico pr', 'sao paulo', 'internacional', 'corinthians', 'fortaleza',
               'goias', 'bahia', 'vasco', 'atletico mg', 'fluminense', 'botafogo', 'ceara', 'cruzeiro', 'csa', 'chapecoense', 'avai')
print('Os 5 Primeiros colocados do Brasileirão 2019')
print('-'*45)
for c in range(5):
    print(f'{c+1}º Colocado: {brasileirao[c].title()}')
print('')
print('Os 4 Últimos colocados do Brasileirão 2019')
print('-'*50)
for i in range(-4, 0, 1):
    print(f'{i+21}º Colocado: {brasileirao[i].title()}')
print('')
print('A Tabela do Brasileirão de 2019 em ordem alfabética')
print('-'*45)
for u in sorted(brasileirao):
    print(u.title())

print('')
print(f'A Chapecoense terminou o Brasileirão 2019 em {brasileirao.index("chapecoense")+1}º colocado')


