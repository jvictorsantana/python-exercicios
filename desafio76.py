# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular. 

mercado = ('Notebook', 1500.00, 'Celular', 2000.00, 'Televisão', 2500.00,
           'Geladeira', 3500.00, 'Cama', 899.99, 'Caneta', 3.00,
           'Grampeador', 4.99, 'Mochila', 37.98
           )
cont = 1
print(f'{" "*10} LISTAGEM DE PREÇO{" "*10}')

for i in range(0, len(mercado), 2):
    print(f'{mercado[i]}', end=' ')
    print(f'{"."*(30- len(mercado[i]))}R$ {mercado[cont]:.2f}')
    cont += 2


