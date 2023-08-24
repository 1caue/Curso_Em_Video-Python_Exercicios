print('-' * 42)
print('{:^42}'.format('LISTAGEM DE PREÇOS'))
print('-' * 42)
p = ('Lápis', 1.75,
    'Borracha', 2,
    'Caderno', 15.90, 
    'Estojo', 25, 
    'Transferidor', 4.20, 
    'Compasso',9.99, 
    'Mochila', 120.32, 
    'Canetas', 22.30, 
    'Livros', 34.90)
for i in range(0, len(p)):
   if i % 2 == 0: 
    print(f'{p[i]:.<30}', end=' ')
   if i % 2 == 1:
    print(f'R${p[i]:>9.2f}') 
