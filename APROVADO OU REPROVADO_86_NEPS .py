A = input()
B = input()
#media = 0

#media = float(media)

A=float(A)
B=float(B)

media = (A+B)/2

if media >= 7:
    print("Aprovado")
if media < 7 or media >= 4 :
   print("Recuperação")
else:
    print("Reprovado")