# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar
# para cada palavra, quais são as suas vogais. 

# palavra = ('mainy'), 'joao', 'santos', 'python', 'maya', 'dudy', 'neymar', 'celular', 'play 5')
palavra = ('mainy', 'joao', 'neymar', 'santos', 'celular', 'maya', 'play 5')

for l in palavra:
    print(f'\nNa palavra {l.upper()} temos: ', end= '')
    for i in l:
        if i in 'aeiouy':
            print(i.upper(), end='')
            


    
        