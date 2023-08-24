s = cont = med = mai = men = 0
resp = 'Ss'
while resp in 'Ss':
    n = int(input('Digite um número: '))
    s += n
    cont += 1
    if cont == 1:
         mai = men = n
    else:
        if n > mai:
            mai = n
        if n < men:
            men = n
    resp = str(input('Quer continuar?[S/N]: ')).upper()[0]
med = s / cont
print(f'Você digitou {cont} números e a média foi {med}')
print(f'O maior valor foi {mai} e o menor foi {men}')
