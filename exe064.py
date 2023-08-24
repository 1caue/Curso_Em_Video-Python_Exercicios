n = cont = som = 0
while n != 999:
    n = int(input('Digite um número [999 para parar]: '))
    cont += 1
    som += n
print(f'Você digitou {cont - 1} números e a soma entre eles foi {som - 999}')
