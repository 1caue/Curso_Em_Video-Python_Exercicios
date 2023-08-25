print('=' * 15)
print('Gerador de PA')
print('=' * 15)
pt = int(input('Primeiro termo: '))
rp = int(input('Razão da PA: '))
term = pt 
c = 1
tot = 0
m = 10
while m != 0: 
    tot = tot + m   
    while c <= tot:
            print(term, '->', end=' ')
            term += rp
            c += 1
    print('PAUSA')
    m = int(input('Quantos termos você quer mostrar a mais: '))
print('FIM')
