from random import randint
print('''Crie um programa que faça o computador jogar Jokenpô com você.
- Pedra 
- Papel 
- Tesoura 
''')
N1 = str(input('Digite sua escolha: '))
L1 = str('Pedra')
L2 = str('Papel')
L3 = str('Tesoura')
Lista = [L1 or L2 or L3]
Computador = randint (L1 or L2 or L3)
print('{}'.format(Computador))
if N1 == 1 and Computador == L3:
    print('Você escolheu Pedra e seu Oponente Tesoura! VOCÊ VENCEU! ')
elif N1 == 1 and Computador == L2:
    print('Você escolheu Pedra e seu Oponente Papel! VOCÊ PERDEU! ')
elif N1 == 2 and Computador == L3:
    print('Você escolheu Papel e seu Oponente Tesoura! VOCÊ PERDEU! ')
elif N1 == 2 and Computador == L1:
    print('Você escolheu Papel e seu adversário escolheu Pedra! VOCÊ VENCEU! ')
elif N1 == 3 and Computador == L1:
    print('Você escolheu Tesoura e seu adversário Pedra! VOCÊ PERDEU!')
elif N1 == 3 and Computador == L2:
    print('Você Tesoura e seu adversário Papel! VOCÊ VENCEU! ')
