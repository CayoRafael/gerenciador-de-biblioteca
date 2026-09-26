print(''' CALCULADORA DE IMC:
– Abaixo de 18,5: Abaixo do Peso
- Entre 18,5 e 25: Peso Ideal
– 25 até 30: Sobrepeso
– 30 até 40: Obesidade
– Acima de 40: Obesidade Mórbida
''')
Peso = float(input('Digite seu peso em Kg: '))
Altura = float(input('Digte sua Altura em Metros: '))
IMC = Peso / (Altura**2)
if IMC <= 18.5:
    print('Seu IMC  é {:.1f} você está \033[1;32m ABAIXO DO PESO!\033[m '.format(IMC))
elif IMC >=18.5 and IMC <= 25:
    print('Seu IMC  é {:.1f} Você tem o \033[1;32m PESO IDEAL!\033[m '.format(IMC))
elif IMC > 25 and IMC <= 30:
    print('Seu IMC  é {:.1f} Você tem um pouco de \033[1;32m SOBREPESO!\033[m Faça exércicios ou uma dieta. '.format(IMC))
elif IMC > 30 and IMC <= 40:
    print('Seu IMC  é {:.1f} Você apresenta \033[1;32m OBESIDADE!\033[m  Precisa cuidar mais a sua saúde. Faça exércicios e dieta.'.format(IMC))
elif IMC > 40:
    print('Seu IMC  é {:.1f} Você apresentou \033[1;32m OBESIDADE MORBIDA!\033[m  Necessita de cuidar urgente da saúde; Faça exércicios e dieta. '.format(IMC))