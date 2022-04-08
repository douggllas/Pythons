segundos = int(input())
#556

horas = segundos//3600
segundos = segundos - horas *3600
minutos = segundos // 60

minutos = segundos //60
segundos = segundos - minutos*60
segundos = segundos

osSegundos = segundos

print (horas)
print (minutos)
print (segundos)

print ('{}:{}:{}'.format(horas,minutos,segundos)) 


'''
n = int(input())
h = n // 60**2
n = n - h * 60**2

m = n // 60
n = n - m*60

s = n

print('{}:{}:{}'.format(h, m, s))

'''