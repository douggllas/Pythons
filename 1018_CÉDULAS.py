cedulas = int(input())
#576
print (cedulas)

cedulas100 = cedulas//100 #Crio a variavel cedulas100 que irá receber quantas cedulas de 100 tem na minha entrada
cedulas = cedulas - cedulas100*100 #Antes de saber quantas cedulas, preciso dividir a entrada por 100, depois faço a subtração e multiplico

cedulas50 = cedulas//50
cedulas = cedulas - cedulas50*50

cedulas20 = cedulas//20
cedulas = cedulas - cedulas20*20

cedulas10 = cedulas//10
cedulas = cedulas - cedulas10*10

cedulas5 = cedulas//5
cedulas = cedulas - cedulas5*5







cedulas2 = cedulas//2
cedulas = cedulas - cedulas2*2

cedulas1 = cedulas//1
cedulas = cedulas - cedulas1*1

print('{} nota(s) de R$ 100,00'.format(cedulas100))
print('{} nota(s) de R$ 50,00'.format(cedulas50))
print('{} nota(s) de R$ 20,00'.format(cedulas20))
print('{} nota(s) de R$ 10,00'.format(cedulas10))
print('{} nota(s) de R$ 5,00'.format(cedulas5))
print('{} nota(s) de R$ 2,00'.format(cedulas2))
print('{} nota(s) de R$ 1,00'.format(cedulas1))





