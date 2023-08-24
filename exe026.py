f = str(input('Digite uma frase: ')).strip().upper()
print(f'A letra aparece {f.count("A")} Vezes na frase')
print(f'A primeira letra A apareceu na posição {f.find("A")+1}')
print(f'A ultima letra apareceu na posição {f.rfind("A")-1}')
