N1 = int(input('\033[1;32m Digite um número: '))
N2 = int(input('\033[1;33m Digite outro número: '))
if N1 > N2:
    print('\033[m O primeiro escolhido {} Valor é maior que o segundo {}: '.format(N1,N2))
elif N2 > N1:
    print('\033[m O segundo valor escolhido {} é maior que o primeiro'.format(N2,N1))
elif N1 == N2:
    print('\033[m Os valores do primeiro {} e do segundo escolhidos {} são iguais: '.format(N1,N2))
