#Faça um programa que leia o nome completo de uma pessoa
#mostrando em seguida o primeiro e o último nome separadamente
#EX: Ana Maria de Souza
# - primeiro = Ana
# - último = Souza

nome = input('Digite seu nome completo: ').strip().split()
print(f'Primeiro nome = {nome[0]}\nSobrenome = {nome[-1]}') #Utilizamos o split para separar a string, e utilizamos o [0] para trazer o primeiro nome
# e o [-1] para trazer o último nome, o -1 geralmente vai representar a última posição de algo que estamos buscando.