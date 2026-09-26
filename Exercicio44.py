print('{:=^40}'.format(' LOJAS TACI RISADINHA ') )
Valor = float(input('Digite o valor da compra: '))
print(''' Formas de pagamento:
[Digite 1] – à vista dinheiro/cheque: 10% de desconto. 
[Digite 2] – à vista no cartão: 5% de desconto.        
[Digite 3] – em até 2x no cartão: preço Normal.        
[Digite 4] – 3x ou mais no cartão: 20% de juros.       
''')
FP = int(input('Qual forma de pagamento? '))
if FP == 1:
    print('Sendo á vista a compra tem 10% e o valor ficará {:.2f} Reais '.format(Valor - Valor *10/100))
elif FP == 2:
    print('Comprando a vista no cartão o desconto é 5 e o valor ficará {:.2f} Reais' .format(Valor - Valor * 5/100))
elif FP == 3:
    print('Compra em 2x de {:.2f} Reais no cartão e o preço final ficará {:.2f} Reais sem acréscimos de juros no valor. '.format(Valor/2,Valor))
elif FP == 4:
    Valor20 = Valor + (Valor * 20 / 100)
    Parc = int(input('Quantas parcelas deseja? '))
    print('Sua compra será parcelada em {:.2f}x de {:.2f} Reais. '.format(Parc,Valor20/Parc))
    print('E o valor final da compra que seria {:.2f} será com acréscimo de 20% de juros {:.2f} Reais.'.format(Valor,Valor20))
else:
    print(' OPÇÃO IMVÁLIDA DE PAGAMENTO! TENTE NOVAMENTE! ')