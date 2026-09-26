'''Faça um programa que mostre a tabuada de vários números, um de cada vez,
para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo.
'''
print('=-=-=-=-=-=-= \033[1;34m GERADOR DE TABUADAS \033[m =-=-=-=-=-=-= ')
print('\033[1;33m→ DIGITE QUALQUER NÚMERO PARA SABER SUA TABUADA:💬 \033[m')
print('\033[1;31m→ PARA ENCERRAR DIGITE UM NÚMERO NEGATIVO! ❌⛔ \033[m')
n = 1
c = 0
while True:
    print('=-=-=-=' * 7)
    n = int(input('\033[1;32m→ A TABUADA DE QUE NÚMERO VC QUER SABER?  \033[m'))
    if n < 0:
        break
    print(f'A TABUADA DE {n} É:')
    print('=-=-=-=' * 7)
    for c in range(1,11):
        print(f'{n} x {c} = {n*c}')
print('=-=-=-=' * 7)
print('FIM DO PROGRAMA! 👍😁')
print('=-=-=-=' * 7)
