n = str(input('Digite a expressão: '))
l = []
for c in n:
    if c == '(':
        l.append('(')
    elif c == ')':
        if len(l) > 0:
            l.pop()
        else:
            l.append(')')
            break
if len(l) == 0:
    print('Sua expressão está Válida')
else:
    print('Sua expressão está Errada')
    