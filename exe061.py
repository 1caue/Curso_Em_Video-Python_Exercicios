print('=' * 15)
print('Gerador de PA')
print('=' * 15)
pt = int(input('Primeiro termo: '))
rp = int(input('Razão da PA: '))
t = pt 
c = 1
while c <= 10:
    print(t, '->', end=' ')
    t = t + rp
    c += 1
print('FIM')
