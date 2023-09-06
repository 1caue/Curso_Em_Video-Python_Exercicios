v = []
while True:
    v.append(int(input('Digite um valor: ')))
    r = str(input('Quer continuar? [S/N] ')).strip().upper()
    if r in 'Nn':
        break
print('-=' * 30)
print(f'Você digitou {len(v)} elementos')
v.sort(reverse=True)
print(f'A ordem dos elementos em ordem decresente é {v}')
if 5 in v:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista')
