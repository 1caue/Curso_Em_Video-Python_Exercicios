import defs

n = int(input('Digite o preço: R$'))
print(f'A metade de {defs.moeda(n)} é {defs.moeda(defs.met(n))}')
print(f'O dobro de {defs.moeda(n)} é {defs.moeda(defs.dob(n))}')
print(f'Aumentando 10%, temos {defs.moeda(defs.dez(n, 10))}')
