from time import sleep
num = int(input('Digite um número inteiro: '))
sleep(1)
print('''Escolha a sua opção
[ 1 ] Converter para BINÁRIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL''') 
sleep(1)
n = int(input('Sua opção: '))
if n == 1:
    print(f'{num} convertido para BINÁRIO é igual a {bin(num)[2:]}')
elif n == 2:
    print(f'{num} convertido para OCTAL é igual a {oct(num)[2:]}')
elif n == 3:
    print(f'{num} convertido para HEXADECIMAL é igual a {hex(num)[2:]}')
else:
    print('Opção invalida tente novamente')
    