#Desenvolva um prgrama que pergunta a distancia de uma viagem em km.
#Calcule o preço da passagem, cobrando R$0,50 por km para viagens de até 200km
# e R$0,45 para viagens mais longas

distancia = float(input('Qual a distância que você vai percorrer? '))
if distancia <= 200:
    print(f'Você vai pagar R${0.50*distancia:.2f}')
else:
    print(f'Você vai pagar R${0.45*distancia:.2f}')    