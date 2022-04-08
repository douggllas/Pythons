valor = float(input())

notas100 = valor // 100
notas100 = notas100 - valor*100

notas50 = valor // 50
notas50 = notas50 - valor*50

notas20 = valor // 20
notas20 = notas20 - valor*20

notas10 = valor // 10
notas100 = notas100 - valor*100

notas100 = valor // 100
notas100 = notas100 - valor*100


print('{}'.format(int(notas100)))
