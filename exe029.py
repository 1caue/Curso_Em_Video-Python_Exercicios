carro = float(input('Qual a velocidade do carro? '))
if carro <= 80:
    print('Você está dentro do limite, parabéns!')
else:
    print('Você passou do limite...')
    km = (carro - 80) * 7
    print('O total a pagar são R${:.2f}'.format(km))