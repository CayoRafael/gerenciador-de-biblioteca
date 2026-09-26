from time import sleep
v1 = int(input('PRIMEIRO VALOR: '))
v2 = int(input('SEGUNDO VALOR: '))
Op = 0
while Op != 5:
    print('''
    [1] - SOMA;
    [2] - MULTIPLICAÇÃO;
    [3] - MAIOR
    [4] - NOVOS NÚMEROS 
    [5] - SAIR... ''')
    Op = int(input('Escolha a sua opção: '))
    if Op == 1:
        Soma = v1 + v2
        print('A soma entre os números {} + {} é igual a {}'.format(v1, v2, Soma))
    elif Op == 2:
        multiplicar = v1 * v2
        print('O resultado da multiplicação entre {} x {} é igual a {}'.format(v1, v2, multiplicar))
    elif Op == 3:
        if v1 > v2:
            print('O maior valor escolhido foi {}'.format(v1))
        else:
            print('O maior valor escolhido foi {}'.format(v2))
    elif Op == 4:
        v1 = int(input('Digite um número novo: '))
        v2 = int(input('Digite outro número novo: '))
    elif Op == 5:
        print('Saindo do Programa!')
    else:
        print('opção inválida. tente outra vez!')
    print('=-='*20)
    sleep(1)
print('Fim do programa, VOLTE SEMPRE!')
