maisv = 0 
maioridadehom = 0
nomev = ''
totmu20 = 0
for c in range(1, 4+1):
    print(f'\033[33m----- \033[32m{c}a PESSOA \033[33m------\033[m')
    n = str(input('Nome: ')).strip()
    i = int(input('Idade: '))
    s = str(input('Sexo [M/F]: ')).strip()
    maisv += i
    if c == 1 and s in 'Mm':
        maioridadehom = i
        nomev = n    
    elif s in 'Mm' and i > maioridadehom:
        maioridadehom = i
        nomev = n 
    elif i < 20 and s in 'Ff':
        totmu20 =+ 1
medi = maisv / 4
print(f'A média de idade do grupo é de {medi} anos')
print(f'O homem mais velho tem {maioridadehom} anos e é o {nomev}')
print(f'E  temos {totmu20} com menos de 20 anos')