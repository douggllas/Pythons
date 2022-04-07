A = int(input())
B = int(input())

if (A>B):
    maior = A
    menor = B
if (B>A): 
    maior = B
    menor = A
for i in range (menor, maior+1):
    print(i, end=" ")