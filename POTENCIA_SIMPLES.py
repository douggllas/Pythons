def main():
    n = float (input())
    k = float (input())

    pot = 1
    i   = 0
    while i < k:
        pot = pot * n
        i   = i + 1
    
    print("A potencia eh %0.4f", pot)  # print mais simples
   
#-----
main()
