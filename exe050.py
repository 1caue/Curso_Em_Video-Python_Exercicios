som = 0 
cont = 0
for c in range (1, 7):
    n = int(input('Digite o valor: '))
    if n % 2 == 0:
        som += n
        cont += 1
print(f'Você informou os valores {cont} e a soma entre eles é {som}')
