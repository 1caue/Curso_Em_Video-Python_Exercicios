l = []
p = []
maip = menp = 0
while True:
    l.append(str(input('Nome: ')))
    l.append(float(input('Peso: ')))
    if len(p) == 0:
        maip = menp = l[1]
    else: 
        if l[1] > maip:
            maip = l[1]
        if l[1] < menp:
            menp = l[1]
    p.append(l[:])
    l.clear()
    r = str(input('Quer continuar?: ')).strip().upper()
    if r in 'N':
        break
print('-=' * 30)
print(f'Ao todo você cadastrou {len(p)} pessoas.')
print(f'O maior foi de {maip} peso de', end=' ')
for a in p:
    if a[1] == maip:
        print(f'[{a[0]}]', end=' ')
print()
print(f'O menor foi de {menp}', end=' ')
for a in p:
    if a[1] == menp:
        print(f'[{a[0]}]', end=' ')
print()
