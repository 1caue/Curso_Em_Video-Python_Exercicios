from time import sleep
pv = int(input('Primeiro valor: '))
sv = int(input('Segundo valor: '))
op = 0
while op != 5:
    sleep(0.5)
    print('\033[33m-=\033[m' * 30)
    print('''             [1] somar  
             [2] multiplicar 
             [3] maior      
             [4] novos números
             [5] sair do programa''')  
    op = int(input('>>>>> Qual é a sua opção?: '))
    if op == 1:
        print(f'A soma entre {pv} e {sv} é {pv + sv}')
    elif op == 2:
        print(f'O resultado de {pv} x {sv} é {pv * sv}')
    elif op == 3:
        if pv > sv:
            print(f'Entre {pv} e {sv} o maior é {pv}')
        else:
            print(f'Entre {pv} e {sv} o maior é {sv}')
    elif op == 4:
        print('Informe os números novamente')
        pv = int(input('Primeiro valor: '))
        sv = int(input('Segundo valor: '))
    elif op == 5:
        print('Até a proxima')
    else:
        print('\033[31mERRO\033[m, Digite um número válido')
        