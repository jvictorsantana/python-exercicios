#Escreva um programa que leia a velocidade de um carro.
#Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$7,00 por cada km acima do limite

velocidade = float(input('Qual a velocidade do carro? '))
if velocidade > 80:
    print(f'Você ultrapassou o limite de velocidade, vai receber uma multa de R${7*(velocidade - 80):.2f}')    
print('Tenha um bom dia, dirija com cuidado!')    