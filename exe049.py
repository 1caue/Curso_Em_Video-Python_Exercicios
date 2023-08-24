n = int(input('Digite um número para ver sua tabuada: '))
print('\033[33m-=\033[m' * 30)
for c in range (1, 11):    
    print(f'{n} x {c} = {n * c}')
print('\033[33m-=\033[m' * 30)