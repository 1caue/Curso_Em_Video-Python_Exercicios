p = float(input('Qual é seu peso? (kg) '))
a = float(input('Qual a sua altura? (m) '))
imc = p / (a ** 2)
if imc < 18.5:
    print(f'Seu IMC é de {imc:.2f}\nVocê está abaixo do peso, procure ajuda')
elif imc > 18.5 and imc < 25:
    print(f'PARABÉNS, seu IMC é de {imc:.2f}\nvocê está no peso ideal')
elif imc > 25 and imc < 30:
    print(f'Seu IMC é de {imc:.2f}\nVocê está com Sobrepeso')
elif imc > 30 and imc < 40:
    print(f'Seu IMC é de {imc:.2f}\nVocê está obeso, procure ajuda')
elif imc > 40:
    print(f'Seu IMC é de {imc:.2f}\nVocê está com obesidade mórbida, procure ajuda imediatamente')
