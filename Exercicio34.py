print('''Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
Para salários superiores a R$1250,00, calcule um aumento de 10%. 
Para os inferiores ou iguais, o aumento é de 15%. ''')
salario = float(input('Qual valor do seu salário: R$  '))
if salario > 1250:
    print('Você recebeu um aumento de 10% em seu salário e agora receberá: {:.2f} reais '.format(salario+salario*10/100))
else:
    print('Você recebeu um aumento de 15% em seu salário e agora receberá: {:.2f} reais '.format(salario+salario*15/100))