import math
from math import sqrt

nome = input ('Qual seu nome? ')
print ('Prazer em te conhecer: {:=^10}!'.format (nome))
CO = float(input('Comprimento do Cateto Oposto: '))
CA = float(input('Comprimento do Cateto Adjacente: '))
Soma = ((CO**2) + (CA**2))
print('Qual valor da hipotenusa? {:.2f}'.format(sqrt(Soma)))
print ('SENO,COS,TANGENTE')
An = float(input('Digite o Angulo que você deseja:'))
Seno = math.sin(math.radians(An))
Cosseno = math.cos(math.radians(An))
Tangente = math.tan(math.radians(An))
print ('O seno é:{:.2f} o Cosseno {:.2f} e a tangente {:.2f}'.format(Seno,Cosseno,Tangente))