def met(n=0, formato=False):
   r = n / 2
   return r if not formato else moeda(r)
 

def dob(n=0, formato=False): 
   r = n * 2
   return r if not formato else moeda(r)
  

def dez(n, t, formato=False):
   r = n + (n * t / 100)
   return r if formato is False else moeda(r)


def dim(preço=0, taxa=0, formato=False):
   r = preço - (preço * taxa/100)
   return r if formato is False else moeda(r)


def moeda(preço=0, moeda='R$'):
   return f"{moeda}{preço:.2f}".replace('.', ',')
