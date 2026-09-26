from random import randint
from time import sleep
itens = ('Pedra', 'Papel','Tesoura')
computador = randint (0,2)
print(''' Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA
''')
print('-='*10)
Jogador = int(input('Qual sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
print('Computador jogou {}'.format(itens[computador]))
print('Jogador Jogou {}'.format(itens[Jogador]))
print('-='*10)
if computador == 0: #computador jogou PEDRA
      if Jogador == 0:
          print('EMPATE')
      elif Jogador == 1:
          print('jOGADOR VENCE')
      elif Jogador == 2:
          print('COMPUTADOR VENCE')
      else:
          print('Jogada inválida!')
elif computador == 1: #computador jogou PAPEL
    if Jogador == 0:
        print('COMPUTADOR VENCE')
    elif Jogador == 1:
        print('EMPATE')
    elif Jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('Jogada inválida!')
elif computador == 2:  #computador jogou TESOURA
    if Jogador == 0:
        print('JOGADOR VENCE')
    elif Jogador == 1:
        print('COMPUTADOR VENCE')
    elif Jogador == 2:
        print('EMPATE')
    else:
        print('Jogada inválida!')
print('-='*10)
