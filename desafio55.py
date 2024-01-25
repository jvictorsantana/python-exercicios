#Faça o programa que leia o peso de 5 pessoas, e no final mostre qual foi o maior e o menor pesos lidos.

peso = []
for c in range(5):
    pessoas = float(input(f'Pessoa nº {c + 1}, digite o seu peso: '))
    peso.append(pessoas)
print(f'O maior peso é de {max(peso)} Kg')
print(f'O menor peso é de {min(peso)} Kg')