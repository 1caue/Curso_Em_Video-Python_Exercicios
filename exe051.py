print('=' * 20)
print('10 TERMOS DE UMA PA')
print('=' * 20)
p1 = int(input('Primeiro Termo: '))
r = int(input('Razão: '))
d = p1 + (10 - 1) * r
for c in range(p1, d + r, r):
    print(c , '->',  end=' ')
print('ACABOU')
