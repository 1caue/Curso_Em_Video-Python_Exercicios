from time import sleep
nome = str(input('Qual é o seu nome completo? ')).strip()
dividir = (nome.split())
juntar = ''.join(dividir)
print('Analisando seu nome...')
sleep(1.5)
print(f'Seu nome em  maiúsculas é {nome.upper()}\n'
      f'Seu nome em minúsculas é {nome.lower()}\n'
      f'Seu nome tem ao todo {len(juntar)} letras\n'
      f'Seu primeiro nome é {dividir [0]} e tem {len(dividir[0])} letras')
