'''CRIE UM PROGRAMA QUE LEIA VÁRIOS NÚMEROS INTEIROS PELO TECLADO
O PROGRAMA SÓ VAI PARAR QUANDO O USUÁRIO DIGITAR O VALOR 999.
QUE É A CONDIÇÃO  DE PARADA.
NO FINAL MOSTRA QUANTOS NUMEROS FORAM DIGITADOS E QUAL FOI A SOMA ENTRE ELES.
(DESCONSIDERANDO O FLAG)'''
print('A SEGUIR DIGITE VALORES PARA QUE SE POSSA REALIZAR OPERAÇÕES: ')
print('PARA INICIAR ATRIBUA QUALQUER VALOR! ')
tot = 1
soma = 0
cont = 0
while tot != 999:
    valor = int(input('DIGITE UM VALOR: '))
    print('PARA ENCERAR O PROGRAMA DIGITE O NÚMERO 999! ')
    print(f'{valor}')
    tot = valor
    soma += valor
    cont += 1
    if tot == 999:
        soma = soma - 999.
        cont -= 1
        med = soma/cont
        print(f'FORAM DIGITADOS {cont} VALORES, A SOMA DELES É {soma:.0f} E A SUA MÉDIA FOI: {med:.1f}!')
print('FIM DE PROGRAMA!')