pm = 0
mv = 0
for c in range(1, 7+1):
    n = float(input(f'Peso da {c}a pessoa: '))
    if c == 1:
        mv = n
        pm = n
    else:
        if n > mv:
            mv = n
        if n < pm:
            pm = n
print(f'O maior peso inserido foi de {mv}kg')
print(f'O menor peso inserido foi de {pm}kg')
