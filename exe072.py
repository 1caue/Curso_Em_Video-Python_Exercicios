n = int(input('Digite um número entre 0 e 20: '))
t = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez'
t2 = 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte'
t3 = t + t2
if n > 20:
    n = int(input('Erro!, Digite um numero entre 0 e 20: '))
print(f'Você digitou o número {t3[n]}')
