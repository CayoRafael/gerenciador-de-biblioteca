print('Faça um programa que leia um número qualquer e mostre sua fatorial')
N1 = int(input('Digite um número: '))
c = N1
fat = 1
print('Calculando {}! = '.format(N1),end='')
while c > 0:
    print(f'{c}', end='')   #print('{}'.format(c)) mesma coisa #,end='' é pra não pular de linha.
    if c > 1:
        print(' x ', end='') # outra forma: print(' x ' if c > 1 else ' = ', end= '')
    else:
        print(' = ', end='')
    fat *= c
    c -= 1
print(f'{fat}', end='')

#from math import factorial
#N1 = int(input('Digite um número: '))
#print(f'{factorial(N1)}')