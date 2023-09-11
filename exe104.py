# Declaração de Defs 
def leiaInt(n):
    ok = False
    v = 0
    while True:
        a = str(input(n))
        if a.isnumeric():            
            v = int(a)
            ok = True
        else:
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')         
        if ok:
            break
    return v


# Programa Principal
f = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {f}')

