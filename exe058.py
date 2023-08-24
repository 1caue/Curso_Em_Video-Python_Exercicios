from random import randint
pc = randint(0, 10)
print('\033[33m-=\033[m' * 30)
print('Vou pensar em um número entre 0 e 10')
acertou = False
totvzs = 0
while not acertou:
    j = int(input('Tente advinhar.....'))
    totvzs += 1
    if j == pc:
        acertou = True
    else:
        if j < pc:
            print('Mais...Tentente mais uma vez')
        elif j > pc:
            print('Menos...Tente mais uma vez')
print(f'Acertou com {totvzs} tentativas. Parabéns!')
print('\033[33m-=\033[m' * 30)
