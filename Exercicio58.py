#'''melhore o jogo do desafio 028 onde o computador vai pensar em um numero entre 0 e 10.
#só que a agora o jogador vai tentar advinhar até acertar.
#mostrando no final quantos palpites foram necessarios pra vencer.''''''
from random import randint
print('=== JOGO DA ADVINHAÇÃO === ')
print('=== SOU SEU COMPUTADOR...===')
print('Acabei de pensar em um número entre 0 e 10. será que você consegue advinhar qual foi?')
print('QUAL O SEU PALPITE? ')
acertou = False
tentativas = 0
Computador = randint (0 , 10)
while not acertou:
    Palpite = int(input(' Digite um palpite entre 0 e 10: '))
    tentativas += 1
    if Palpite == Computador:
        acertou = True
    else:
        if Palpite < Computador:
            print('Mais.. tente mais uma vez. ')
        elif Palpite > Computador:
            print('Menos...Tente mais uma vez.')
print('O numero secreto era {} e você aertou com {} tentativas'.format(Computador,tentativas))
