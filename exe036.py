vc = float(input('Qual o valor da casa?: R$'))
sc = float(input('Qual o salário do comprador?: R$'))
f = int(input('Quantos anos de financiamento?: '))
ff =  vc / (f * 12) 
print(f'Para pagar uma casa de \033[32mR${vc}\033[32m em {f} anos a pestação será de \033[32mR${ff:.0f}\033[m!')
if sc / 2 < ff:
    print('\033[31mO salario do comprador é muito pouco, EMPRÉSTIMO NEGADO\033[m')
else: 
    print('\033[32m EMPRÉSTIMO CONCEDIDO\033[m')
