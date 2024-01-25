#DEsenvolva um programa que leia o comprimeito de três retas e diga ao usuário se elas podem ou não formar um triângulo.
print('-=-'*20)
print('ANALISANDO TRIANGULOS')
print('-=-'*20)

a = int(input('Digite a: '))
b = int(input('Digite b: '))
c = int(input('Digite c: '))
if a + b > c and b + c > a and a + c > b:
    print('Pode formar um triângulo!')
else:
    print('Não pode formar um triangulo!')    