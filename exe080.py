v = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > v[-1]:
        v.append(n)
        print('Adicionado no fim da lista...')
    else:
        p = 0
        while p < len(v):
            if n <= v[p]:
                v.insert(p, n)
                print(f'Adicionado a posição {p} da lista')
                break
            p += 1
print('=-' * 30)
print(f'Os valores digitados em ordem foram {v}')
