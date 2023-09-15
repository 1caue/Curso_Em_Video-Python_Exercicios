def met(n):
   return n / 2

def dob(n): 
   return n * 2

def dez(n, t):
   r = n + (n * t / 100)
   return r 

def moeda(preço=0, moeda='R$'):
   return f"{moeda}{preço:.2f}".replace('.', ',')
