print('-' * 15)
print('Sequência de Fibonacci')
print('-' * 15)
n = int(input('Quantos termos quer mostrar?: '))
print('~' * 15)
p = 0
s = 1
cont = 0 
while cont <= n:
    t = p + s
    print(t, '->', end=' ')
    p = s
    s = t
    cont += 1
print('FIM')
