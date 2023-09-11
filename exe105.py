def notas():
    c = 0
    while True:
        l = int(input('Digite a nota: '))
        c += 1
        if sn in 'SN':
            sn = str(input('Quer continuar? [S/N] ')).strip().upper()
            if sn in 'Nn':
                break
    print(f'Foram digitadas {c} notas\nA maior nota foi {l(max)}')
notas()

