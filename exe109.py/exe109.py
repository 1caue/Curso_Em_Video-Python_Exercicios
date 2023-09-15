import defs

n = int(input('Digite o preço: R$'))
print(f'A metade de {defs.moeda(n)} é {defs.met(n, True)}')
print(f'O dobro de {defs.moeda(n)} é {defs.dob(n, True)}')
print(f'Aumentando 10%, temos {defs.dez(n, 10, True)}')
print(f'Diminuindo 13% temos {defs.dim(n, 13, True)}')
