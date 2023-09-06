l = [[], []]
v = 0
for c in range(1, 8):
   v = int(input(f'Digite o {c}o valor: '))
   if v % 2 == 0:
       l[0].append(v) 
   if v % 2 == 1:
       l[1].append(v)
print('-=' * 30)
l[0].sort()
l[1].sort()
print(f'Os valores pares digitados foram: {l[0]}')
print(f'Os valores impares digitados foram: {l[1]}')
