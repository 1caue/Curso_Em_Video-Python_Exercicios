from time import sleep
from random import randint
print('\033[33m-=\033[m' * 30)
nu = int(input('\033[36mVou pensar em um número entre 0 e 5. Tente advinhar...\033[m: '))
n = randint(0, 5)
print('\033[31mPROCESSANDO...\033[m')
sleep(1)
if nu == n:
    print('Parabens, Você acertou')
else:
    print('Você errou, tente novamente')
print('\033[33m-=\033[m' * 30)