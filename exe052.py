n = int(input('Digite um número: '))
tot = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[32m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print(c, end=' ')
print(f'\033[m\nO número {n} foi divisivel {tot} vezes')
if tot == 2:
    print('\033[33mPor isso ele é primo\033[m')
else:
    print('\033[31mPor isso ele não é primo\033[m')
