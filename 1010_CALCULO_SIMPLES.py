linha1 = input().split(" ")
linha2 = input().split(" ")

codigo, qtd, valor = linha1
codigo2, qtd2, valor2 = linha2

total = (int(qtd)*float(valor))+(int(qtd2)*float(valor2))
print("VALOR A PAGAR: R$ %0.2f" % total)
