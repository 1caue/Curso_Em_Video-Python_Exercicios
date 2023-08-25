s = float(input('QUAL SEU SALÁRIO ATUAL: R$'))
if s > 1250:
    print(f'Quem ganhava R${s} agora ganhará R${s * 1.1}')
elif s <= 1250:
    print(f'Quem ganhava R${s} agora ganhará R${s * 1.15}')