from math import sqrt
o = float(input('Digite o comprimento do cateto oposto: '))
a = float(input('Digite o comprimento do cateto adjacente: '))
h1 = (o ** 2) + (a ** 2)
h2 = sqrt(h1)
print(f'A hipotenusa vai medir {h2:.2f}')
