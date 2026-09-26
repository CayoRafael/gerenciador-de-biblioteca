'''Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:
considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.'''
print('=-'*16)
print('{:.^30}'.format('BANCO MASTER 🔰💲🏦'))
print('{:.^30}'.format('CAIXA ELETRONICO 🤑'))
print('=-'*16)
print('ESTA MÁQUINA POSSUI CEDULAS')
print('DE R$50, R$20, R$10 e R$1. ')
print('=-'*16)
Saque = float(input('QUAL VALOR EM R$ DESEJA SACAR: '))
tot = Saque
ced = 50
totced = 0
while True:
    if tot >= ced:
        tot -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'\033[1mTotal de {totced} cédulas de {ced} R$ \033[m')
        if ced == 50:
            ced = 20
            totced = 0
        elif ced == 20:
            ced = 10
            totced = 0
        elif ced == 10:
            ced = 1
            totced =0
        if tot == 0:
            break
print('=-'*21)
print('O BANCO MASTER AGRADECE A PREFERÊNCIA! 🔰💲🏦')
print('=-'*21)


