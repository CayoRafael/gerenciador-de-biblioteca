nome = str(input('Qual seu nome? '))
if nome == 'Cayo':
    print('\033[1;36m Que lindo nome!')
elif    nome == 'Maria' or nome == 'Taciana' or nome == 'Jade':
    print('\033[1;33m Esse nome é bem popular no Brasil:')
elif nome in 'Taciana Fernandes Paixão':
    print('\033[1;31;m Belo nome feminino!')
else:
    print('\033[1;35m Seu nome é bem normal!')
print('\033[1;32m Tenha um bom dia!\033[2;35m {}\033[m'.format(nome))
