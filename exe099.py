from time import sleep

def valor(* num):
    c = mai = 0
    print('-=' * 30)
    print('Analisando os valores passados...')
    for v in num:
        print(f'{v} ', end='', flush=True)
        sleep(0.5)
        if c == 0:
            mai = v
        else:    
            if v > mai:
                mai = v
        c += 1
    print(f'Foram informados {c} valores ao todo')
    print(f'O maior valor informado foi {mai}')

# Programa Principal
valor(2, 9, 4, 5, 7, 1)
valor(4, 7, 0)
valor(1, 2)
valor(6)
valor()
