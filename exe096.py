def cdt(l, c):
    a = l * c 
    print(f'A área de um terreno {l}x{c} é de {a}m²')


# Programa Principal
print('Controle de terrenp')
print('-' * 30)
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
cdt(c=c, l=l)
