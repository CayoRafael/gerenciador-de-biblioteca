from shlex import split

nome = str(input('Digite o nome de sua cidade: ')).strip()
NS = ('Santo,santo' in nome )
print ('Existe a palavra Santo no nome da cidade? {}'.format(NS))
