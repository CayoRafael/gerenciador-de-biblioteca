import emoji
n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print(emoji.emojize('Prazer em te conhecer! :grinning_face:'))
print('Seu primeiro nome é: {}'.format(nome[0]))
print('Seu último nome é: {}  '.format(nome[len(nome)-1]))