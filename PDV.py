total_de_vendas = 0
qtd_de_vendas = 0

while True:
  print ("\n---- minha loja - pdv -----")
  print ("1 - Registrar venda ")
  print ("2 - Ver relatório do dia ")
  print ("3 - Encerrar Caixa ")
  if opcao == "0":
    print("encerrando o caixa até amanhã")
    break

  elif opcao == "1":
    produto = input ("Nome do produto: ")
    valor = float(inpu("Valor do produto: R$ "))
    percentual = float(nput("Desconto (%): "))

  valor_final = calcular_desconto (valor,percentual)

  if valor_final is None:
    print("Desconto inválido: Use um valor entre 0  100 ")
  else:
    valor_final = arredondar(valor_final)
    registrar_venda(produto,valor_final)
    total_vendas = total_vendas + valor_final
    qtd_vendas = qtd_vendas + 1

  elif opcao == "2":
    print(f" \n vendas hoje: (qtd_vendas)")
    print(f"total faturado: R$ (arrendondar (total_vendas))")

else:
print("opção inválida. tente de novo. ")

