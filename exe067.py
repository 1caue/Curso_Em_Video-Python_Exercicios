while True:
    print('-' * 45)
    n = int(input('Quer ver a tabuada de qual valor?: '))
    print('-' * 45)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {n * c}')
print('PROGRAMA DE TABUADA ENCERRRADO, volte sempre!')
