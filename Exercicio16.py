from math import trunc, sqrt, hypot
from os.path import realpath

N1 = float(input(' Digite um número: '))
print ('O valor desse número é {} e sua porção inteira é: {} '.format(N1,trunc(N1)))
N2 = float(input('Digite um valor '))
print ('O valor desse número é {} e sua porção inteira é: {} '.format(N2,int(N1)))
print ('TRIGONOMETRIA')
co = float(input('Comprimento do Cateto Oposto: '))
ca = float(input('Comprimento do Cateto Adjacente: '))
hi = hypot(co,ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))