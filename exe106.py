from time import sleep
# Cores
cores = ('\033[m', # 0 Sem cor
     '\033[0;30;41m', # 1 Vermelho
     '\033[0;30;42m', # 2 Verde
     '\033[0;30;43m', # 3 Amarelo
     '\033[0;30;43m', # 4 Azul
     '\033[0;30;44m', # 5 Roxo
     '\033[0;30;45m' # 6 Branco
     )

# Def's
def a(com):
   t(f'Acessando o manual do comando \'{com}\'', 4)
   print(cores[0], end='')
   help(com)
   print(cores[0], end='')
   sleep(1) 

def t(msg, cor=0):
    tam = len(msg) + 4
    print(cores[cor], end='')
    print('~' * tam)
    print(f' {msg}')
    print('~' * tam)
    print(cores[0], end='')
    sleep(1)

# Programa Principal
c = ''
while True:
    t('SISTEMA DE AJUDA PyHELP', 2)
    c = str(input('Função ou Biblioteca = '))
    if c.upper() == 'FIM':   
        break
    else:
        a(c)
t('ATÉ LOGO', 0)

