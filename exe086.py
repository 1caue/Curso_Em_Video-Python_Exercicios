#     0   1   2
l = [[0,0,0], [0,0,0], [0,0,0]]
for x in range(0, 3):
    for y in range(0, 3):
        l[x][y] = int(input(f'Digite um valor para a posição [{x}, {y}]: '))
print('-=' * 30)      
for x in range(0, 3): 
    for y in range(0, 3):
        print(f'[{l[x][y]:^5}]', end=' ')
    print()
