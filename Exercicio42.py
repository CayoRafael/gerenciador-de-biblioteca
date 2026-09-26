print('''Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

– EQUILÁTERO: todos os lados iguais
– ISÓSCELES: dois lados iguais, um diferente
– ESCALENO: todos os lados diferentes
''')

L1 = float(input('\033[1;32m Digite valor para o lado: '))
L2 = float(input('\033[1;33m Digite um valor para o outro lado: '))
L3 = float(input('\033[1;34m Digite um valor para o terceiro \033[m'))
if L1 < L2 + L3 and L2 < L1 + L3 and L3 < L1 + L2:
    print('Os seguimentos podem formar um TRIANGULO: ')
    if L1 == L2 == L3:
        print('\033[1;32m EQUILÁTERO!\033[m :  ')
    if L1 != L2 !=L3 !=L1:
        print(' \033[1;32m ESCALENO\033[m :')
    else:
        print(' \033[1;32m ISOCELES\033[m:  ')
else:
    print('Os seguimentos Não podem formar um triangulo: ')



