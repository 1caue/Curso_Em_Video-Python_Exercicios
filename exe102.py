# Declaração de def ⤵
def fatotial(a, show=True):
        '''Calcula o fatorial de um número.
           'A' será o parâmetro que será
           Calculado no programa principal 
           Já o "show=True ou false, será o  
           parãmetro que irá mostrar o calculo
           no terminal        
        '''
        
        r = 1 
        for c in range(a, 0, -1):
            if show:
                print(c, end='')
                if c > 1:
                    print(' x ', end='')
                else:            
                    print(' = ', end='')
            r *= c
        return r
        

# Programa pricipal ⤵
print('-' * 40)
n = int(input('Digite um número para ver seu fatorial: '))
print(fatotial(n, show=True))
h = str(input('Quer ver como o programa funciona?: [S/N] ')).upper().strip()
if h in 'Ss':
    print(help(fatotial))
    