t18 = tHOM = tMV = 0
while True:
    print('-' * 25)
    print('CADASTRE UMA PESSOA')
    print('-' * 25)
    i = int(input('Idade: '))
    s = ' '
    while s not in 'MF':
        s = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if i >= 18:
        t18 += 1
    if s == 'M':
        tHOM += 1
    if s == 'F' and i < 20:
        tMV += 1
    c = ' '
    while c not in 'SN':
        print('-' * 25)
        c = str(input('Quer continuar?: [S/N] ')).strip().upper()[0]
    if c == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {t18}')
print(f'Ao todo temos {tHOM} homens cadastrados')
print(f'E temos {tMV} mulheres com menos de 20 anos')
