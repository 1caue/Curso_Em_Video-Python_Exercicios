n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
if n1 > n2:
    print(f'O número {n1} é maior do que o {n2}')
elif n2 > n1:
    print(f'O número {n2} é maior do que o {n1}')
else:
    print('Os dois valores são IGUAIS')