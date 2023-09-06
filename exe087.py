par = mai = tc =  mai = 0
#       0        1        2
l = [[0,0,0], [0,0,0], [0,0,0]]
for x in range(0, 3):
    for y in range(0, 3):
        l[x][y] = int(input(f'Digite um valor para a posição [{x}, {y}]: '))
print('-=' * 20)
for x in range(0, 3):
    for y in range(0, 3):
        print(f'[{l[x][y]:^5}]', end=' ')
        if l[x][y] % 2 == 0:
            par += l[x][y]
    print()
print('-=' * 20)
print(f'A soma dos valores pares é {par}')
for x in range(0, 3):
    tc += l[x][2]
print(f'A soma dos valores da terceira coluna é {tc}')
for y in range(0, 3):
    if y == 0:
        mai = l[1][y]
    elif l[1][y] > mai:
        mai = l[1][y]    
print(f'O maior valor da segunda linha é {mai}')
