from datetime import date
Atual = date.today().year
ANO = int(input('QUAL O ANO EM QUE VOCÊ NASCEU? '))
ID = Atual-ANO
if ID <= 9:
    print('VOCÊ TEM {} ANOS PORTANTO SE ENQUADRA NA CATEGORIA MIRIM'.format(ID))
elif ID >= 10 and ID <= 14:
    print('VOCÊ TEM {} ANOS PORTANTO PERTENCE A CATEGORIA INFANTIL:'.format(ID))
elif ID  >= 15 and ID <=19:
    print('VOCÊ TEM {} ANOS, PORTANTO SUA CATEGORIA É A JUNIOR: '.format(ID))
elif ID >=20 and ID <= 25:
    print(' VOCÊ TEM {} ANOS, PORTANTO SUA CATEGORIA É A SÊNIOR:'.format(ID))
else:
    print('VOCÊ TEM {} ANOS, PORTANTO SUA CATEGORIA É A MASTER:'.format(ID))

