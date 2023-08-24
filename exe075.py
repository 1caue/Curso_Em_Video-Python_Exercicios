n1 = (int(input('Digite um número: ')), int(input('Digite mais um número: ')), 
      int(input('Digite outro número: ')), int(input('Digite o último número: ')))
print(f'Você digitou os valores {n1}')
print(f'O valor 9 apareceu {n1.count(9)} vezes')
if 3 in n1:
    print(f'O valor 3 apareceu na {n1.index(3)+1}ª posição')
else:
    print(f'O valor 3 não apareceu em nenhuma posição')
print('Os valores pares digitados foram', end=' ')
for n in n1:
    if n % 2 == 0:
        print(n, end=' ')
        