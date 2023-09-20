def dint(msg):
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


def real(msg):
    while True:
        try:
            r = float(input(msg))
        except(ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número real valido\033[m')
            continue
        except(KeyboardInterrupt):
            print('\n\033[31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0 
        else:
            return r
i = dint('Digite um valor inteiro válido: ')
r = real('Digite um valor real válido: ')
print(f'O valor inteiro digitado foi {i} e o real foi {r}')
