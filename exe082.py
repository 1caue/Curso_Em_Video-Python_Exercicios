from time import sleep
p = []
i = []
num = []
while True:
    num.append(int(input('Digite um número: ')))
    r = str(input('Quer continuar? [S/N] ')).strip().upper()
    if r in 'Nn':
        break
for a, b in enumerate(num):
    if b % 2 == 0:
        p.append(b)
    elif b % 2 == 1:
        i.append(b)
print('=-' * 30)
sleep(1)
print(f'A lista completa é {num}')
sleep(1)
print(f'A lista de pares é {p}')
sleep(1)
print(f'A lista de impares é {i}')
