# Crie um programa que tenha uma tupla totalmente preenchida com contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

numeros = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito',
           'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis',
            'dezesete', 'dezoito', 'dezenove', 'vinte')
while True:
    numero = int(input('Digite um número entre 0 e 20 '))
    if numero >= 0 and numero <= 20:
        print(numeros[numero])
    else:
        print('Tente novamente, apenas de 0 a 20')