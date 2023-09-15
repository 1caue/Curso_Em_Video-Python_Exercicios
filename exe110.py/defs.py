# Def Principal
def resumo(preço=0, taxa=10, taxr=5):
   print('-=' * 15)
   print('RESUMO DO VALOR'.center(30))
   print('-=' * 15)
   print(f'Preço Analisado:     {moeda(preço)}')
   print(f'Dobro do preço:      {dob(preço, True)}')
   print(f'Metade do preço:     {met(preço, True)}')
   print(f'20% de Aumento:      {dez(preço, 20, True)}')
   print(f'12% de redução:      {dim(preço, 12, True)}')
   print('-=' * 15)


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

