print ('Qual Novo Salário')
Salario = int (input ('Qual salário?'))
Aumento = (Salario * (15/100))
SalarioFin = Salario + Aumento
print ('O salário com aumento de 15% é: {}'.format (SalarioFin))
print ('Desconto')
VP = int (input ('Qual valor do produto?'))
VD = VP * (5/100)
VF = VP - VD
print ('O valor do produto com desconto de 5% é: {} R$' .format (VF))
print ('Convertendo em dolares')
Cart = int (input ('Quanto você tem na carteira? '))
Dolar = Cart / 5.86
print ('Convertendo o valor em dolares você tem: {}'.format (Dolar))

