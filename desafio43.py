#Desenvolva uma lógica que leia o peso e a altura de uma pessoa. Calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# Abaixo de 18.5: Abaixo do peso
# Entre 18.5 e 25: Peso Ideal
# 25 até 30: Sobrepeso
# 30 até 40: Obesidade
# Acima de 40: Obesidade Mórbida
peso = float(input('Informe o seu peso: '))
altura = float(input('Informe a sua altura: '))
imc = peso /altura**2
if imc < 18.5:
    print(f'Seu imc é de {imc:.1f}, você esta abaixo do peso!')
elif imc == 18.5 or imc < 25:
    (print(f'Seu imc é de {imc:.1f}, você está no peso ideal!'))
elif imc == 25 or imc< 30:
    (print(f'Seu imc é de {imc:.1f}, você está no sobrepeso!'))
elif imc == 30 or imc <40:
    (print(f'Seu imc é de {imc:.1f}, você está obeso!'))    
else:
    (print(f'Seu imc é de {imc:.1f}, você está com OBESIDADE MÓRBIDA!'))    