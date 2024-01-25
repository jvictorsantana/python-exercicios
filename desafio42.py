#Refaça o desafio 35 dos triangulos, acrescentando o recurso de informar que tipo de triangulo sera formado
# Equilátero: todos os lados iguais
# Isóceles: dois lados iguais
# Escaleno: todos os lados diferentes

print('-=-'*20)
print('ANALISANDO TRIANGULOS')
print('-=-'*20)

a = int(input('Digite a: '))
b = int(input('Digite b: '))
c = int(input('Digite c: '))
if a + b > c and b + c > a and a + c > b:
    print('Pode formar um triângulo!')
    if a == b and b == c:
        print('TRIANGULO EQUILÁTERO')    
    elif a == b or a==c and b!=c or b==c and a!=c:
        print('TRIANGULO ISÓCELES')    
    elif a!= b or a!=c and b!= c:
        print('TRIANGULO ESCALENO')
else:
    print('Não pode formar um triangulo!') 
