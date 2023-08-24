print('\033[33m=-\033[m' * 30)
print('VAMOS JOGAR PAR OU IMPAR')
print('\033[33m=-\033[m' * 30)
from random import randint
from time import sleep
cont = 0
pc = v = 0
while True:
    pc = randint(0, 10)
    v = int(input('Diga um valor: '))
    t = ' '
    r = pc + v
    while t not in 'PI':
        t = str(input('Par ou impar? [P/I]: ')).upper().strip()[0]
    sleep(1)
    print(f'Você jogou {v} e o computador {pc}. Total de {r}')
    sleep(1)
    print('Deu par' if r % 2 == 0 else 'Deu Impar')
    if t == 'P':
        sleep(1)
        if r % 2 == 0:
            print('\033[32mVocê VENCEU!\033[0m')
            cont += 1 
        else:
            print('\033[31mVocê PERDEU!\033[0m')    
            break 
    elif t == 'I': 
        sleep(1)
        if r % 2 == 1:
            print('\033[32mVocê VENCEU!\033[0m')
            cont += 1
        else:  
            print('\033[31mVocê PERDEU\033[0m')
            break
    sleep(1)
    print('Vamos novamente')
print('\033[33m=-\033[m' * 30)
print(f'GAME OVER! Você venceu {cont} vezes.')
