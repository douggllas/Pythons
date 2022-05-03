from tkinter import Y


valor  =  input().split
x,y = valor

if x==0: 
    if y==0:
        print('Origem')
    if y!=0:
        print('Eixo Y')
if y==0:
    if x!=0:
        print('Eixo X')
if x>0: 
    if y>0: 
        print('Q1')
    if y<0:
        print('Q4')
if y<0:
    if y<0:
        print('Q3')
    if y>0:
        print('Q2')