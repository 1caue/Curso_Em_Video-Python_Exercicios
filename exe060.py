f = 1 
n = int(input('Digite um número para\nCalcular seu Fatorial: '))
c = n 
while c > 0:
    print(c, end=' ')
    print(' x ' if c > 1 else ' = ', end=' ')
    f = f * c
    c -= 1
print(f)
