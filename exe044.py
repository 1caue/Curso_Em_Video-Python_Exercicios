print('\033[97m========\033[32m OLIVEIRA MAGAZINE \033[97m========\033[m')
preço = int(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO\033[33m 
[ 1 ] Á vista dinheiro/cheque 
[ 2 ] Á vista Cartão
[ 3 ] 2x No cartão   
[ 4 ] 3x ou Mais no cartão\033[m''')
opção = int(input('Qual a sua opção?: '))
if opção == 1:
    av = preço * (10 / 100)
    print(f'Sua compra de R${preço} vai custar R${preço - av} no final')
elif opção == 2:
    avv = preço * (5 / 100)
    print(f'Sua compra de R${preço} vai custar R${preço - avv} no final')
elif opção == 3:
    print(f'Sua compra de R${preço} será parcelada em 2x de R${preço / 2}')
elif opção == 4:
    p = int(input('Quantas parcelas?: '))
    tot =  preço + (preço * 20 / 100)
    parcelado = tot / p
    print(f'Sua compra será parcelada em {p}x de R${parcelado:.2f} COM JUROS')
    print(f'Sua compra de R${preço} vai custar R${tot} no final')
else:
    print('\033[31mOPÇÃO INVALIDA\033[m')
    