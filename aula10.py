import emoji
nome = str(input('Digite um nome: '))
if nome == 'Cayo':
    print(emoji.emojize ('Que nome lindo você tem :growing_heart: '))
else:
    print(emoji.emojize ('Seu nome é tão normal! :expressionless_face: '))
print(emoji.emojize('Bom dia, {} :grinning_face: '.format(nome)))