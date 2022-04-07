# Quadrante
x = int(input())
y = int(input())
# acrescentando as condições
if x == 0 or y == 0:        # Se X = 0X=0 ou Y = 0Y=0, o ponto pertence a um dos eixos.
    print("eixos")
elif x > 0 and y > 0:  # Se X > 0X>0 e Y > 0Y>0, o ponto pertence ao quadrante 1.
    print("Q1")
elif x < 0 and y > 0:  # Se X < 0X<0 e Y > 0Y>0, o ponto pertence ao quadrante 2.
    print("Q2")
elif x < 0 and y < 0:  # Se X < 0X<0 e Y < 0Y<0, o ponto pertence ao quadrante 3.
    print("Q3")
else:
    print("Q4")
