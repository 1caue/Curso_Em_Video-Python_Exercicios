# Def
def notas(*n, sit=False):
    """
    => Função que analisa situação de aluno
    param n = irá realizar as contas e entregar 
    o resultado
    param sit = irá analizar a situação do aluno
    e dar o resultado
    return = irá retornar a situação
    """
    d = {}
    d['total'] = sum(n)
    d['maior'] = max(n)
    d['menor'] = min(n)
    d['media'] = sum(n)/len(n)
    if sit:
        if d['media'] >= 7:
            d['situação'] = 'Boa'
        elif d['media'] >= 5:
            d['situação'] = 'Razoável'
        else:
            d['situação'] = 'Ruim'    
    return d


# Programa principal
n = notas(5, 6, 4, sit=True)
print(n)
