from ctypes.wintypes import FLOAT
from email.errors import InvalidMultipartContentTransferEncodingDefect


nome = (input())
salario = float(input())
vendas = float(input())
comissao = float(salario + (vendas*0.15))

print("TOTAL = R$ %.2f" %comissao)