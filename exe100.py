from random import randint
l = [randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10)]   

def sort():
  print(f'Sorteando os 5 valores da lista: {l} PRONTO!') 

def pair(list):
  s = 0
  for p in list:
    if p % 2 == 0:
        s += p 
  print(f'A soma dos valores pares é {s}')  

sort() 
pair(l)
