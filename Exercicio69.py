'''Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem acima de 20 anos.'''
print('=-=-=-=-='*5)
print('PESQUISA POPULACIONAL IBGE SENSUS 2026 [📊🟢🔵🟡]')
id= 0
cont18 = cont20m = contH = contm18 = 0
part = 0
while True:
    id = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo? - [M/F]: ')).strip().upper()[0]
    opc = ' '
    while opc not in 'SN':
        opc = str(input('Deseja continuar? - [S/N]: ')).strip().upper()[0]
    part += 1
    if id > 18:
        cont18 += 1
    if id < 18:
        contm18 += 1
    if sexo == 'F' and id > 20:
        cont20m += 1
    if sexo == 'M':
        contH += 1
    if opc == 'N':
        print('\033[1;32;40m=-=-= RESULTADOS =-=-=')
        print(f'\033[1;37;40m→ A pesquisa contou com {part} participantes')
        print(f'→ {cont18} participantes tem mais de 18 anos e {contm18} são menores de idade.')
        print(f'→ {contH} participantes eram homens.')
        print(f'→ {cont20m} participantes eram mulheres acima de 20 anos.')
        break
print('Fim do programa 👍✨')