from datetime import date
a = date.today().year
cont = 0
cont2 = 0
for c in range(1, 7 + 1):
    n = int(input(f'Em que ano a {c}a pessoa nasceu?: '))
    print(end='')
    d = a - n 
if d > 18:
    cont += 1
elif d < 18:
    cont2 += 1
print(f'Ao todo tivemos {cont} pessoas maiores de idade')
print(f'E também tivemos {cont2} pessoas menores de idade')