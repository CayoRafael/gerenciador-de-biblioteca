while True:
    id = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo? - [M/F]: ')).strip().upper()[0]
    opc = ' '
    while opc not in 'SN':
        opc = str(input('Deseja continuar? - [S/N]: ')).strip().upper()[0]