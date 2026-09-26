import emoji
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda not: '))
m = (n1 + n2)/2
print('Sua média foi {:.1f}' .format(m))
if m >= 6.0:
    print(emoji.emojize('Sua média foi boa! Parabéns :grinning_face:'))
else:
    print(emoji.emojize('Sua média foi ruim! Estude mais! :pensive_face:'))
