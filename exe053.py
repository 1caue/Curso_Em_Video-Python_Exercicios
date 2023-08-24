n = str(input('Digite uma frase: ')).strip().upper()
p = n.split()
j = ''.join(n)
i = ''
for n in range(len(j) -1, -1, -1):
    i += j[n]
print(f'O inverso de {j} é {i}')
if i == j:
    print('palindromo')
else:
    print('não palindromo')