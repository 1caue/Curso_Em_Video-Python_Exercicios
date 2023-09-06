from time import sleep
from random import randint
jg = []
jg2 = []
print('-' * 30)
print('      JOGA NA MEGA SENA')
print('-' * 30)
n = int(input('Quantos jogos você quer que eu sorteie?: '))
c = 0
while c <= n:
    cont = 0
    while True:
        a = randint(1, 60)
        if a not in jg:
           jg.append(a) 
           cont += 1
        if cont >= 6:
            break
    jg.sort() 
    jg2.append(jg[:])
    jg.clear()
    c += 1
print(f'-=-=-= SORTEANDO {n} JOGOS =-=-=-')
for xs, y in enumerate(jg2):
    print(f'Jogo {xs}: {y}')
    sleep(1)
print('-=-=-=-=-= < BOA SORTE! > =-=-=-=-=-')
