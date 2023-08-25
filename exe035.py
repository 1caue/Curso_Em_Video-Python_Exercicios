s1 = float(input(f'Digite o primeiro seguimento: '))
s2 = float(input(f'Digite o segundo seguimento: '))
s3 = float(input(f'Digite o terceiro seguimento: '))
if (s1+s2) > s3 and (s1+s3) > s2 and (s2+s3) > s1:
    print('Podem formar um triângulo.')
else:
    print('Não podem formar um triângulo.')
    