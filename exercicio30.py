import emoji
Numero = float(input(emoji.emojize('Digite um número: :eyes: ')))
resultado = Numero % 2
print('O resto da divisão do número {:.1f} por 2 é: {:.1f}'.format(Numero,resultado))
if resultado == 0:
    print('Portanto numero {:.1f} é par:'.format(Numero))
else:
    print('Portanto número {:.1f} é impar:'.format(Numero))