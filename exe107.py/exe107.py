import defs

n = int(input('Digite o preço: R$'))
print(f'A metade de {n} é {defs.met(n)}')
print(f'O dobro de {n} é {defs.dob(n)}')
print(f'Aumentando 10%, temos {defs.dez(n, 10):.1f}')
