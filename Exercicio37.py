print('''Escreva um programa em Python que leia um número inteiro qualquer 
e peça para o usuário escolher qual será a base de conversão:
1 para binário, 
2 para octal e 
3 para hexadecimal.''')
N1 = int(input('Digite um número inteiro: '))
print('''Escolha uma das três bases para conversão:
[ 1 ] - Converter em Binário.
[ 2 ] - Converter em octal.
[ 3 ] - Converter em Hexadecimal. ''')
Opcao = int(input('Digite sua opção:  '))
if Opcao == 1:
      print('{} Convertido pra Binário é {}'.format(N1,bin(N1)[2:]))
elif Opcao == 2:
       print('{} Convertido pra Octal é {}'.format(N1,oct(N1)[2:]))
elif Opcao == 3:
       print('{} Convertido pra Hexadecimal é {}'.format(N1,hex(N1)[2:]))
else:
    print('Opção invalida! Tente novamente: ')

