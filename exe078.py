n = [int(input('Digite um valor para a posição 0: ')), int(input('Digite um valor para a posião 1: ')), 
     int(input('Digite um valor para a posião 2: ')), int(input('Digite um valor para a posião 3: ')), int(input('Digite um valor para a posião 4: '))]
ma = max(n)
mi = min(n)
print('-=' * 40)
print(f'Você digitou os valores {n}')
print(f'O maior valor digitado foi {ma} nas posições {n.index(ma)}...')
print(f'O menor valor digitado foi {mi} nas posições {n.index(mi)}...')
