def line():
    return '-' * 42

def leiaint(msg):
    while True:
        try:
            i = int(input(msg))
        except(ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro valido\033[m')
            continue
        except(KeyboardInterrupt):
            print('\n\033[31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
           return i
        

def cab(txt):
    print(line())
    print(txt.center(42))
    print(line())


def menu(lst):
    cab('MENU PRINCIPAL')
    c = 1
    for i in lst:
        print(f'\033[33m{c}\033[m - \033[36m{i}\033[m')
        c += 1
    print(line())
    opc = leiaint('\033[33mSua Opção: \033[m')
    return opc
