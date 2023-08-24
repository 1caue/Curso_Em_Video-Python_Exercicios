totcom = totmil = m = cont = 0
b = ' '
print('-' * 40)
print('{:^40}'.format('LOJA SUPER TUDÃO'))
print('-' * 40)
while True:    
    nomp = str(input('Nome do produto: '))
    preço = float(input('Preço: R$'))
    cont += 1
    totcom += preço
    print('-' * 40)
    if preço >= 1000:
        totmil += 1
    if cont == 1:
        m = preço
        b = nomp
    else:
        if preço < m:
            m = preço
            b = nomp
    res = ' '
    while res not in 'SN':
        res = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    print('-' * 40)
    if res == 'N':
            break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi {totcom}')
print(f'Temos {totmil} produto custando mais de R$1000')
print(f'O produto mais barato foi a {b} custando {m}')
