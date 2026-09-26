'''Crie um programa que leia números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).'''
n = cont = soma = med= 0
while True:
    n = int(input('\033[1m=-= DIGITE UM VALOR: \033[1;31m(999 PARA PARAR):\033[m'))
    if n == 999:
        break
    cont += 1
    soma += n
    med = soma / cont
print(f'Foram digitados {cont} números, a soma entre eles foi {soma} e a média {med}')