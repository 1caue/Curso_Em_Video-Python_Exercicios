=
Nesse readme, Eu fiz um breve resumo sobre de todas as aulas e exercicios passados no curso a partir da aula 6
=
---

**AULA 6 CDP, TIPOS PRIMITIVOS:**

Python possui vários tipos primitivos (também conhecidos como tipos básicos) que são usados para armazenar valores simples. Alguns dos tipos primitivos mais comuns em Python incluem:

Inteiro (int): Representa números inteiros

Ponto Flutuante (float): Representa números decimais.

Booleano (bool): Representa valores lógicos verdadeiro (True) ou falso (False). Usado principalmente em expressões condicionais.

String (str): Representa sequências de caracteres. Pode ser delimitada por aspas simples (' ') ou aspas duplas (" "). 

Nenhum (NoneType): Representa a ausência de valor. É frequentemente usado para inicializar variáveis que serão atribuídas posteriormente

Esses são os tipos primitivos mais comuns em Python. No entanto, Python é uma linguagem dinamicamente tipada, o que significa que você não precisa declarar explicitamente o tipo de uma variável. O interpretador Python de duz o tipo automaticamente com base no valor atribuído à variável.

**Exercicios**

- exe03 CRIE UM PROGRAMA QUE LEIA DOIS NUMEROS E MOSTRE A SOMA ENTRE ELES

- exe04 FAÇA UM PROGRAMA QUE LEIA ALGO PELO   TECLADO E E MOSTRE NA TELA O SEU TIPO PRIMITIVO E TODAS AS INFORMAÇÕES POSITIVAS SOBRE ELE

---

**AULA 7 CDP OPERADORES ARITIMÉTICOS:**
- Operadores Aritméticos
   + Adição           ** Potência
   - Subtração        // Divisão Inteira
   * Multiplicação    %  Resto da Divisão
   / Divisão Única        
- Ordem de Precedência (Ordem pela qual as contas serão executadas primeiro)
   1 - ()   3 - *, /, // e- %
   2 - **   4 - + e -

O "end=' '" serve para não quebrar a linha 
já o " \n " serve para quebrar a linha 

**EXERCICIOS**

 - exe005 Faça um programa que leia um numero inteiro e mostre seu sucessor e seu antecessor

 - exe006 Crie um algoritmo que leia um número e mostre o seu dobro triplo e raiz quadrada
 
 - exe007 Desenvolva um programa que leia as duas notas de um aluno e que calcule e mostre sua média
 
 - exe008 Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros	
 
 - exe009 Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada

 - exe010 Crie um programa que leia quanto de dinheiro uma pessoa tem e mostre quantos dólares ela pode comprar
Considere U$ = R$3,27
 
 - exe011 Faça um programa que leia a largura e altura de uma parede em metros, calcule a sua area e a quantidade de tinta necesaria para pintar-la´, sabendo que cada litro de tinta pinta uma area de 2m2
 
 - exe012 Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto 

---

**AULA 8 CDP UTILIZANDO MODULOS:**
Modulos são como tuplas você irá importá-las de alguma biblioteca

Usando o "from math", você poderá utilizar todas essas funcionalidades 

ceil = arrendodamento para cima
floor = arrendodamento para baixo
trunc = ele irá truncar o numero
pow = potencia (**)
sqtr = calcula a raiz quadrada
factorial = ele irá calcular o fatorial 

Ex: import math
    (Várialvel) = math.sqrt(Várialvel)
    OU
    from math import sqrt
    (Várialvel) = sqrt(Várialvel)

**EXERCICIOS**
 
  exe016 = Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira 
   Ex:Digite um numero: 6.127
      O número 6.127 tem a parte inteira 6
 
 - exe017 = Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triamgulo retangulo, calcule e mostre o comprimento da hipotenusa
 
 - exe018 = Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno cosseno e tangente desse ângulo
 
 - exe019 = Um professor quer sortear um dos seus quatro alunos para apagar o quadro, Faça um programa que leia o nome deles e sorteie o escolhido

 - exe020 = O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada

- exe021 = Faça um progama que abra e reproduza o áudio de um arquivo MP3 

---
 
**AULA 9 CDP MANIPULANDO TEXTO**
 
FATIAMENTO
  - Frase (Curso em Video Python)
  - Contando os caracteres da frase acima temos 21 caracteres, pois o programa lê o caracter começando do 0
  
  - Se declarar uma varialvel 'frase = "Olá mundo"' e mandar dar um print(frase[1]) ele irá retornar o "l" 
  
  - Mas se der um 'print(0:5)' ele irá printar apenas "olá m" pois o programa sempre irá diminuir um
  
  - da mesma maneira se eu der um "print(0:5:2)" o programa irá dar um print pulando de 2 em 2 por conta do '2' no print
  
  - se eu der um 'print(0:)' ele irá dar um print até o final da frase
  
  - 'len(frase)' ele irá contar quantos caracteres tem na frase 
  
  - da mesma maneira o 'frase.count('o') ira contar quantas vezes a letra "o" ou qualquer letra que vc queira contar irá aparecer na frase ou se eu der um 'frase.count('o',0,13) o programa irá procurar quantas letras "o" tem do caractere 0 até o 13
  
  - já o "frase.find('ola')" irá procurar o a palavra "ola" na frase
  
  - o "frase.replace('Olá','ola')" irá trocar as palavras 
  
  - o "frase.upper()" irá colocar todas as letras da frase em maiusculo já o frase.lower() irá colocar todas letras em minusculo
  
  - já o "frase.capitalize()" irá colocar apenas a primeira letra de todas as palavras em maiusculas da mesma maneira o "frase.title()" irá analisar todas as palavras e irá colocar todas as primeiras letras em maiusculo
  
  - o "frase.strip()" irá remover todos os espaços inuteis da frase, usando esse mesmo termo se utilizarmos o "frase.rstrip" ele irá remover todos os espaços vazios da direita e irá manter os da esquerda, já o "frase.lstrip()" irá remover todos os espaços da esquerda e irá manter os da direita
  
  - o "frase.split()" ele irá dividir as palavras da frase
   
**EXERCICIOS**
 
- exe022: Crie um programa que leia o nome completo de uma pessoa e mostre: O nome com todas as letras maiúsculas, o nome com todas as letras minusculas, quantas letras ao todo(sem considerar espaços), quantas letras tem o primeiro nome 

- exe23- faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados Ex: "Digite um número:1834"
              "Unidade: 4"
             "Dezena: 3"
              "Centena: 8"
              "Milhar: 1"

- exe024 - crie um programa que leia o nome e uma cidade e diga se ela começa com ou não com "SANTO"

- exe025: Faça um progama que leia se o nome de uma pessoa e diga se ela tem "SILVA" no nome
 
- exe026: Faça um programa que leia uma frase pelo teclado e mostre: Quantas vezes aparece a letra "A", Em que posição ela aparece a primeira vez e Em que posição ela aparece pela ultima vez

- exe027: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente EX:
Ana Maria de Souza 
Primeiro = Ana
Último = Souza 

---

**AULA 10 CONDIÇÕES PT.1:** 	
Nessa aula o professor pegou de exemplo um caminho e montou dois trajetos

	se carro.esquerda():         else:
	  carro.siga()                carro.siga()      
	  carro.direita()             carro.esquerda()
	  carro.siga()                carro.siga()
	  carro.direita()             carro.esquerda()
	  carro.esquerda()            carro.siga()
	  carro.siga()
	  carro.direita()
	  carro.siga() 
	                 carro.pare()

Independente do caminho o primeiro e o ultimo sempre serão executados

ESTRUTURA CONDICIONAL EM PYTHON
Exemplo em Python:

1: 	

 	if carro.esquerda():
	     bloco true
	   else:
	     bloco false

2:

  	tempo = int(input('Quantos anos tem seu carro?))
	   if tempo <= 3:
	     print('carro novo')
	   else:	
	     print('carro velho')
	   print('--FIM--') 

3. Mesmo comando acima, só que menor

	   tempo = int(input('Quantos anos tem seu carro?'))
	   print('carro novo' if tempo <=3 else 'carro velho')
	   print('--FIM--') 

**Exercicios**
 
- exe028 = Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
  o programa deverá escrever na tela se o usuário venceu ou perdeu
 
- exe029 = Escreva um programa que leia a velocidade de um carro, se ele ultrapassar os 80km, mostre uma mensagem dizendo que ele foi multado, a multa vai custar R$7,00 por cada km acima do limite

- exe030 = Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou IMPAR

- exe031 = Escreva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200km e R$0,45 para viagens mais longas

- exe032 = Crie um programa que leia um ano qualquer e mostre se ele é BISSEXTO
 
- exe033 = Faça um programa que leia três números e mostre qual é o maior e qual é o menor

- exe034 = Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1.250, calcule um aumento de 10% 
Para os inferiores ou iguais a, o aumento é de 15%

- exe035 = Desenvola um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo

---

**AULA 11 CORES NO TERMINAL:**

Codigo ANSI, escape sequence
Toda vez que quiser representar uma cor usará o codigo: 

	\033[m e entre o '[' e o 'm' vc colocará o codigo desejado

e o máximo de codigo entre os dois é de 3. 

EX: 

 	\033[0;33;44m 
 
 o 0 é o estilo o 33 é a cor do texto e o 44 é a cor de fundo, perceba que o codigo finaliza com 'm' e começa com '\033[' 

NÚMEROS CODIGOS PARA ESTILO: 0, 1, 4 e 7
0 = sem estilo nenhum
1 = coloca em negrito
4 = ele vai sublinhar a linha
7 = ele inverte

NÚMEROS CODIGOS PARA TEXTO: 30, 31, 32, 33, 34, 35, 36, 37 e 97
30 = Preto
31 = Vermelho
32 = Verde
33 = Amarelo
34 = Azul 
35 = Roxo
36 = Ciano
37 = Cinza
97 = Branco

NÚMEROS CODIGOS PARA FUNDO: 40, 41, 42, 43, 44, 45, 46, 47 e 107
40 = Preto
41 = Vermelho
42 = Verde
43 = Amarelo
44 = Azul 
45 = Roxo
46 = Ciano
47 = Cinza
107 = Branco
 
Ex de como implementar as cores já no codigo:
a = 1
b = 2
print(f'OS VALORES SÃO \033[35m{a}\033[m e \033[32m{b}\033[m')

Nunca esquecer do '[m'no final do codigo

**Exercicio:**

Colocar cores em pelo menos 15 dos 35 exercicos já feitos 15/15

---

**AULA 12 CONDIÇOES ANINHADAS**

Nessa aula o professor pegou o mesmo exemplo da aula 10, dos caminhos dos carros, porém ele adicionou mais um caminho 

	se carro.esquerda():         
	  carro.siga()                                        
	  carro.direita()             
	  carro.siga()                
	  carro.direita()             
	  carro.esquerda()            
	  carro.siga()
	  carro.direita()    
	  carro.siga()
	
	senão se carro.direita():
	  carro.siga() 
	  carro.esquerda()
	  carro.siga()
	  carro.esquerda()
	  carro.siga()
	
	senão
	  carro.siga()
	carro.pare()

Em Python:
	
 	se = if |
	senão se = elif |
	senão = else.
	Você pode usar o elif quantas vezes quiser, porém não pode ter elif sem if, o else pode ser ou não usado.

**Exercicios:**

- exe036 = Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal sabendo que ela não vai poder exceder 30% do salário ou então o empréstimo será negado.

- exe037 = Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual a base de conversão:
-1 para binário
-2 para octal
-3 para hexadecimal

- exe038 = Escreva um programa que leia dois números inteiros e compare-os mostrando na tela uma mensagem:
  - O primeiro valor é MAIOR
  - O segundo valor é Maior
  - Não existe valor maior os dois são iguais

- exe039 = Faça um programa que leia o ano de nascimeto de um jovem e informe, de acordo com sua idade:
  - Se ele ainda vai se alistar ao serviço militar. 
  - Se é a hora de se alistar. 
  - Se já passou do tempo de alistamento
Seu programa também deverá mostrar o tempo que falta para seu alistamento ou que passou do prazo

- exe040 = Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
  - Média abaixo de 5.0:
REPROVADO
  - Média entre 5.0 e 6.9:
RECUPERAÇÃO
  - Média 7.0 ou superior:
APROVADO 

- exe041 = A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atletae e mostre sua categoria, de acordo com sua idade:
  - Até 9 anos: MIRIM
  - Até 14 anos: INFANTIL
  - Até 19 anos: JUNIOR
  - Até 20 anos: SÊNIOR
  - Acima: Master

- exe042 = Refaça o DESAFIO 042 dos triângulos acrescentando o recurso de mostrar que tipo de triângulo será formado:
  - Equilátero: todos os lados iguais 
  - Isósceles: dois lados iguais 
  - Escaleno: todos os lados diferentes

- exe043 = Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
  - Abaixo de 18.5: Abaixo do peso 
  - Entre 18.5 e 25: Peso ideal
  - 25 até 30: Sobrepeso
  - 30 até 40: Obesidade
  - Acima de 40: Obesidade mórbida

- exe044 = Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
  - Á vista dinheiro/cheque: 10% de desconto
  - Á vista no cartão: 5% de desconto 
  - Em até 2x no cartão: preço normal
  - 3x ou mais no cartão: 20% de juros

- exe045 = Crie um programa que faça o computador jogar jokenpô com você

---

**AULA 13 ESTRUTURA FOR (LAÇOS DE REPETIÇÃO)**

Nessa aula o professor ensinou sobre o laço for dando exemplo de passo a passo
usando o seguinte exemplo:

	laço c no intervalo(1, 10)
	  passo
	pega
	Em python:
	for c in range(1, 10)
	  passo 
	pega

Ex:
 
	Outro exemplo: 
	laço c no intervalo(0,3)
	  passo
	  pula
	passo
	pega
	Em python:
	for c in range(0,3)
	  passo 
	  pula
	passo
	pega

Ex:
 
	Outro exemplo:
	laço c no intervalo(0,3)
	 se 0
	    pega 
	  passo
	  pula
	 passo 
	 pega

Ex python:

	for c in range(0,3)
	 if 0
	    pega
	  passo
	  pula
	 passo
	 pega

na estrutura range de (1, 6)  e (0, 6) 
imagine que você está abrindo várias portas, e da porta  6 você não tem a chave, 
você irá abrir da porta 1 ( ou zero) até onde você tem a chave, quando chegar na porta 6
você PARA porque não tem a chave.
e cada porta que você abriu você diz ' oi '
totalizando 5x ( de 1, 6)
ou totalizando 6x ( de zero a 6)

outra dica é: nunca esqueça em qualquer coisa que seja matemática, O ZERO TAMBÉM É NÚMERO, então sempre conte com ele.

-----------------------------------
Mini Calculadora em python

	s = 0
	for c in range (0, 3):
	    n = float(input(f'Digite o {c+1}º valor para soma: '))
	    s += n
	print(f'{s:.0f}\nFim')
-----------------------------------

**Exercicios:**

- exe046 = Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artificio, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

- exe047 = Crie um programa que mostre na tela todos os números PARES que estão entre 1 e 50

- exe048 = Faça um programa que calcule a soma de todos os números impares que estão são múltiplos de três e que se encontram no intervalo de 1 até 500 

- exe049 = Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for. 

- exe050 = Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for impar, desconsidere-o

- exe051 = Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

- exe052 = Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

- exe053 = Crie um programa que leia uma frase e diga se ela é um palindromo, desconsiderando os espaços

- exe054 = Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

- exe056 = Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos

- exe057 = Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
  - A média de idade do grupo 
  - Qual o nome do homem mais velho.
  - Quantas mulheres têm menos de 20 anos. 

---

**AULA 14 ESTRUTURA DE REPETIÇÃO WHILE:**

Na aula 14 o professor mostrou o exemplo da ultima aula, porem dessa vez a quantidade de blocos para chegar na maça não era númerado, por isso o while tem que ser utilizado 
Ex:

	enquanto não 🍎       
	  passo
	pega
	
Ex python:

 	while not 🍎:
	  passo 
	pega 

Exemplo usando while e if´s:

	enquanto não 🍎
	  se [|]
	    passo
	  se []
	    pula
	  se 0
	    pega
	pega

Ex python:

	while not 🍎:
	 if [|]: 
	   pega
	 elif []:
	   pega
	 elif 0:
	   pega
	pega

Estrutura para girar o codigo várias vezes

	n = 'S' 
	while n == 'S':
	    f = int(input('Digite um valor: '))
	    n = str(input('Quer continuar[S/N]: ')).upper()
	print('fim')

Analisador de números:

	print('DIGITE 0 PARA SAIR')
	n = 1 
	par = impar = 0
	while n > 0:
	    n = int(input('Digite um valor: '))
	    if n != 0:    
	        if n % 2 == 0:
	            par += 1
	        else:
	            impar += 1
	print(f'Você digitou {par} numeros pares e {impar} numeros impares')

**Exercicios**

- exe057 = Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto

- exe058 = Melhore o jogo do desafio 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

- exe059 = Crie um programa que leia dois valores e mostre um menu na tela:
- [1] Somar
- [2] Multiplicar
- [3] Maior
- [4] Novos números 
- [5] Sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.

- exe060 = Faça um programa que leia um número qualquer e mostre o seu fatorial
-  Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120

- exe061 = Refaça o Desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressâo usando a estrutura while.

- exe062 = Melhore o Desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos. o programa encerra quando ele disser que quer mostrar 0 termos.

- exe063 = Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequência de Fibonacci

- exe064 = Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)

- exe065 = Crie um programa que leia vários números inteiros pelo teclado. no final da execução, mostre a média entre todos os valores e qual foi o maior e mmenor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores. 

---

**AULA 15 INTERROMPENDO REPETIÇÕES WHILE:**

Nessa aula o professor usou o mesmo exemplo da aula passada, a do boneco, os blocos de grama e a maça, só que dessa vez foi inserido um troféu na plataforma e caso o boneco achasse esse troféu ele pararaia toda a sua tragetoria 
Ex em algoritmo:

 	enquanto Verdadeiro
	   se [|] 
	     passo
	   se [ ]
	     pula
	   se 0 
	     pega
	   se 🏆
	     pula 
      	   pega
	interrompa	

Em python:

 	while True:
	  if [|]
	    passo
	  if [ ]
	    pula
	  if 0
	    pega
	  if 🏆
	    pula 
	    break
	pega

O comando break serve sempre para jogar o programa para fora de uma estrutura de repetição

O comando break tem sempre que ficar após a pergunta para o usuário ex:

 	c = s = 0
	while True:
	    c = int(input('Digite um número: '))
	    if c == 999:
	        break
	    s += c
	print(f'A soma vale {s}')

**Exercicios**

- exe066 = Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag) 

- exe067 = Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo

- exe068 = Faça um programa que jogue par ou impar com o computador. O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

- exe069 = Crie um programa que leia a idade e o sexo e várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
a) quantas pessoas tem mais de 18 anos.
b) quantos homens foram cadastrados.
c) quantas mulheres tem menos de 20 anos.

- exe070 = Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final mostre:
A) Qual é o total gasto na compra.
B) Quantos produtos custam mais de R$1000.
C) Qual é o nome do produto mais barato.

- exe071 = Crie um programa que simule o funcionamento de um caixa eletrônico. No inicio, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.  

---

**AULA 16 VÁRIAVEIS COMPOSTAS (TUPLAS):**

Tuplas são váriaveis que armazenam vários dados porem esses dados não podem ser modificados após a tupla ser criada ex:

Variável simples = "c = maça"

Tupla = "c = maça, banana, uva, pera"

Lembrando sempre que a enúmeração de dados na tupla sempre vai começar por zero ex:

	tupla = "c = maça, banana, uva, pera"
	               0     1      2     3

se a váriavel for declararada uma assim: 

	c = 'maça', 'uva', 'banana', 'pera'

e der um print(c[1]), ele irá printar a "uva", mas se eu der um print(c[-1]) ele irá printar a pera 

dá pra utilizar o metodo "len()" tambem ex:
	
 	len(c) = 4 (a tupla "c" tem 4 elementos)

as estrutura de repetição tambem podem ser utilizadas ex:

	c = maça, banana, uva, pera
	for b in c:                     o b receberá o c várias vezes até o c for igual a pera                                                    
	 print(b)                       após isso o codigo irá continuar fora dessa estrutura

nesse codigo abaixo o for irá printar todas as comidas até chechar na pera, quando chegar ne pera ele irá sair do codigo e irá dar o ultimo print

	c = ('maça', 'uva', 'banana', 'pera')
	for b in c:
	    print(f'Eu vou comer {b}')
	print('comi muito')

usando o len() ele irá contar a quantidade de elementos na estrutura ex:

	c = ('maça', 'uva', 'banana', 'pera')
	for b in range (0, len(c)):
	    print(f'vou comer {c[b]}')

porém se utilizarmos o 'enumerate()' ele irá printar o que é que está na tupla e a sua posição ex:

	c = ('maça', 'uva', 'banana', 'pera')
	for pos, comida in enumerate(c):
	  print(f'vou comer {comida} na posição {pos}')

nesse codigo acima ele irá printar o que é que sera comido e a sua posição

utilizando o metodo "sorted()" ele ira organizar o codigo ex:

	c = ('maça', 'uva', 'banana', 'pera')
	print(sorted(c))

 ⇧ Ele irá printar ['banana', 'maça', 'pera', 'uva']

Para somar duas tuplas é facil apenas iremos precisar de uma váriavel que some as duas ex:

 	c = (1, 2, 3, 4)
	b = (5, 6, 7, 8)
	a = c + b
	print(a.count(1))
	print(a.index(1))

o ".count()" irá contar a quantidade de vezes que o numero 1 aparece

já o print(a.index(1)) irá procurar em que posição está o numero 1 

Lembrando que as TUPLAS SÃO IMUTÁVEIS, se vc declarou c = ('maça', 'uva', 'banana', 'pera'), ele não poderá atribuir mais nada nas outras linhas de codigo

**Exercicios**

- exe072 = Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado e mostrá-lo por extenso.

- exe073 = Crie uma tupla preenchida com os 20 primeiros colocados da tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
A) Apenas os 5 primeiros colocados.
B) Os ultimos 4 colocados da tabela.
C) Uma lista com os times em ordem alfabética.
D) Em que posição na tabela está p time da chapecoense.

- exe074 = Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla, Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

- exe075 = Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final mostre:
  - A) Quantas vezes apareceu o valor 9.
  - B) Em que posição foi digitado o primeiro valor 3.  
  - C) Quais foram os números pares.

- exe076 = Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços na sequência.
No final, mostre uma listagem de preços, organizando os dados em forma tabular.

- exe077 = Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais

---

**Aula 17 Variáveis Compostas (Listas) Pt.1:**

Nessa aula o professor falou sobre a semelhança entre tuplas e listas, porém elas não são 100% iguais, diferente das tuplas, Listas são mutavéis ex:

	lanche = ['maça', 'uva', 'pera', 'banana']
	lanche[3] = 'manga' 
	print(lanche)  

nesse exemplo o codigo irá printar 'maça', 'uva', 'pera', 'manga' 

Tuplas()
Listas[]

e como visto acima as listas são declaradas com [], e para atribuir algo a lista usa o comando .append() ex:

	lanche = ['maça', 'uva', 'pera', 'banana']
	lanche.append('manga')
	print(lanche)

nesse comando ele irá printar 'maça', 'uva', 'pera', 'banana', 'manga'

E para inserir um elemento antes de outro elemento é so utilizar o metodo .insert(numero do elemento onde deseja inserir,'') ex:

	lanche = ['maça', 'uva', 'pera', 'banana']
	lanche.append('manga')
	lanche.insert(0, 'laranja')
	print(lanche)

nesse comando ele irá printar 'laranja', 'maça', 'uva', 'pera', 'banana' ,'manga', O elemento que era 0 virou 1 o que era 1 virou 2 o que era 2 virou 3 e assim vai

e as maneiras de apagar um elemento na lista são, usando o 'del lanche [núm. elemento]' ou '.pop(núm. elemento)' ou '.remove('elemento')', se vc colocar o '.pop()' sem nenhum elemento a ser apagado ele irá eliminar o ultimo número

se vc colocar um 'valores = list(range(4, 11)) 
ele criará uma lista com os valores indo de 4 até 10

se vc criar uma lista uma lista com os valores 8, 2, 5, 4, 9, 3, 0 e der um .sort ele irá orgaziar os valores de forma crescente
ex: 

 	valores = [8, 2, 5, 4, 9, 3, 0]
	valores.sort()
	print(valores)

ele irá imprimir '0, 2, 3, 4, 5, 8, 9'

para colocar os valores de maneira decrescente é só colocar o metodo .sort() novamente e dento das () é só colocar o metodo
'reverse=True', lembrando que o "True" tem que começar com T maiúsculo ex:

	valores = [8, 2, 5, 4, 9, 3, 0]
	valores.sort()
	valores.sort(reverse=True)
	print(valores)

valores vão ser 9, 8, 5, 4, 3, 2, 0

e usando o 'len()' ele irá contar quantos elementos tem no codigo, no exemplo acima ele terá 7 elementos

se vc igualar uma lista na outra ele criará uma ligação entre as mesmas ex:

	a = [2, 3, 4, 7]
	b = a
	b[2] = 8
	print(f'Lista A: {a}')
	print(f'Lista B: {b}')

ele irá printar
Lista A: [2, 3, 8, 7]
Lista B: [2, 3, 8, 7]

para quebrar essa ligação é só colocar o b = a[:] 

**Exercicios**

- exe078 = Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista

- exe079 = Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valorees únicos digitados, em ordem crescente

- exe080 = Crie um programa onde o usuário possa digitar cinco valores númericos e cadastre-os em uma lista, já na posição correta de inserção(sem usar o sort()). No final, mostre a lista ordenada na tela. 

- exe081 = Crie um programa que vai ler vários números e colocar em uma lista. 
Depois disso, mostre:
a)Quantos números foram digitados.
b)A lista de valores, ordenada de forma decrescente.
c)Se o valor 5 foi digitado e está ou não na lista.

- exe082 = Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores impares digitados, respectivamente. Ao final, mostre o conteúdo das três listas gerados. 

- exe083 = Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta. 

---

**AULA 18 Variáveis compostas (Listas) Pt.2:**

No começo da aula o professor revisou os assuntos passados na última aula e Nessa aula o professor irá ensinar como criar uma lista dentro da outra
Ex: 

			0              1             2
	pessoas = [['Pedro', 25], ['Maria', 19], ['João', 32]]
	               0      1       0      1       0     1

Isso é, dentro da lista "pessoas" eu tenho 3 listas

E se eu der um "print(pessoas[0][0])"
	ele irá printar 'Pedro' 

Outro exemplo utilizando as Variáveis compostas acima ⇧: 

	print(pessoas[1][1])
ele irá printar '19'
	
	print(pesssoas[2][0]) 
ele irá printar 'João'
	
	print(pessoas[1])
ele irá printar tudo 'Maria', 19

Outro exemplo::

	galera = [['João', 14], ['Pedro', 15], ['Felipe', 15], ['Gabriel', 14]]
	for c in galera:
	    print(f'{c[0]} tem {c[1]} anos')

ele irá printar:
-	João tem 14 anos
-	Pedro tem 15 anos
-	Felipe tem 15 anos
-	Gabriel tem 14 anos

Caso queira uma copia da lista não esquecer do [:] ex: 

	g = []
	d = []
	for c in range(0, 3):
	    d.append(str(input('Nome: '))) 
	    d.append(int(input('Idade: ')))   
	    g.append(d[:])
	    d.clear()
	print(g)

No código acima ele copia o de antes apaga-ló
Codigo completo

	g = []
	d = []
	totmen = totmai = 0
	for c in range(0, 3):
	    d.append(str(input('Nome: '))) 
	    d.append(int(input('Idade: ')))   
	
 	# Abaixo ele irá copiar o codigo antes de apagar
	    g.append(d[:])
	    d.clear()
	
 	# Ele irá verificar se o individuo é maior de idade
	for p in g:
	    if p[1] >= 18:
	        print(f'{p[0]} é maior de idade.')
	        totmai += 1
	    else: 
	        print(f'{p[0]} é menor de idade.')
	        totmen =+ 1
	print(f'Temos {totmai} maiores e {totmen} menores.')
 
**Exercicios**

- exe084 = Faça um programa que leia o nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
a)Quantas pessoas foram cadastradas.
b)Uma listagem com as pessoas mais passadas.
c)Uma listagem com as pessoas mais leves. 

- exe085 = Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e impares. No final, mostre os valores pares e impares em ordem crescente.

- exe086 = Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final mostre a matriz na tela, com a formatação correta.

- exe087 = Aprimore o desafio anterior, mostrando no final: 
a) A soma dos valores pares digitados.
b) A soma dos valores da terceira coluna.
c) O maior valor da segunda linha. 

- exe088 = Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

- exe089 = Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

---

**AULA 19 VARIÁVEIS COMPOSTAS (DICIONÁRIOS)**

Nessa aula o professor ensinou como declarar dicionários usando o seguinte exemplo 

                        dados
		    'Pedro' 25	
			0    1

se eu der um: dados = dict() ou dados = {}, o programa ficará assim:

	dados = {}
	dados = {'nome':'Pedro', 'idade':25}

o indicie 0 dos dados passará a valer 'nome' e o indicie 1 passará a valer 'idade', usando o mesmo programa acima e dando um print() ele ficará assim: 

                         dados
		    'Pedro'   25     	
	             nome    idade  

	dados = {}
	dados = {'nome':'Pedro', 'idade':25}
	print(dados['nome']) 
	print(dados['idade'])

ele irá printar 'Pedro' e 25

diferente das listas ou das tuplas os dicionários não precisam do ".append()" para atribuir uma váriavel, para atribuir basta dar um "dados['sexo'] = M, e ele ficará assim:

                           dados
		    'Pedro'   25     M	
	              nome   idade  sexo

e se eu quiser eliminar um elemento basta apenas utilizar o comando 'del', ex

	dados['sexo'] = 'M' 
	del dados['idade']

                           dados
		     'Pedro'    M	
	              nome     sexo

Agora vamos criar um elemento:

	filme = {'titulo': 'Star Wars',
	         'ano': 1977,
		 'diretor': 'George Lucas'
	 	 }	 	

e o python entenderá assim:
 
		    filme
	'Star wars'  1977   'George Lucas'
          titulo     ano        diretor
 
se eu der um print(filme.values()), ele irá retornar a parte de cima (os valores), mas se eu quiser pegar a parte de baixos(as chaves) é só eu dar um print(filme.keys()), mas se eu quiser pegar todos os valores é só dar um print(filme.items())

Agora vamos utilizar o for com os dicionários da seguinte maneira:

	for k, v in filme.items():
		print(f'O {k} é {v)')

ele irá printar:
O titulo é Star Wars
    {k}        {v}
O ano é 1977
  {k}    {v}
O diretor é George Lucas     
    {k}         {v}

Dá pra se utilizar também dicionários com listas ex:
 LOCADORA
'Star wars'  1977   'George Lucas'   / 	 'Avengers'  2012    'Joss Whedon'   /  'Matrix'   1999     'Wachowski'
  titulo     ano        diretor     /      titulo     ano      diretor      /    titulo     ano       diretor         
	 	  
se eu der um:
print(locadora[0]['ano'])     ele irá printar 1977
print(locadora[2]['titulo'])  ele irá printar 'Matrix'

--------------------------------------------------------
Codigos importantes:

Para dar um print em um dicionário:
	
 	dados = {'nome': 'Caue', 'idade': '19', 'sexo':'M' }
	print(f'O {dados["nome"]} tem {dados["idade"]} anos')


Para ver todos os itens do dicionário:

	dados = {'nome': 'Caue', 'idade': '19', 'sexo':'M' }
	print(dados.items())
	print(dados.keys())
	print(dados.values())

Para printar todos os valores e apagar um elemento:

 	dados = {'nome': 'Caue', 'idade': '19', 'sexo':'M' }
	del dados['idade']
	for k, v in dados.items():
	    print(f'{k} = {v}')
 
Para modificar:

	dados = {'nome': 'Caue', 'idade': '19', 'sexo':'M' }
	dados['nome'] = 'junior'
	for k, v in dados.items():
	    print(f'{k} = {v}')

Para adicionar elementos:

	dados = {'nome': 'Caue', 'idade': '19', 'sexo':'M' }
	dados['peso'] = 98.5
	for k, v in dados.items():
	    print(f'{k} = {v}')

O 'peso' não existe por isso ele adicionou

Para criar Lista com dicionários:

 	br = []
	e1 = {'uf': 'Bahia', 'Sigla': 'BA'}
	e2 = {'uf': 'São Paulo', 'Sigla': 'SP'}
	br.append(e1)
	br.append(e2)
	print(br)

e caso queira printar algo especifico nesse mesmo codigo

 	br = []
	e1 = {'uf': 'Bahia', 'Sigla': 'BA'}
	e2 = {'uf': 'São Paulo', 'Sigla': 'SP'}
	br.append(e1)
	br.append(e2)
	print(br[1]["uf"])
-----------------------------------------------------------

**Exercicios**

- exe090 = Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela. 
 
- exe091 = Crie um programa onde 4 jogadores jogem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado

- exe092 = Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre os (com idade) em um dicionário se por acaso a ctps for diferente de ZERO. o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

- exe093 = Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

- exe094 = Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
  - A Quantas pessoas foram cadastradas 
  - B A média de idade do grupo.
  - C Uma lista com todas as mulheres.
  - D Uma lista com todas as pessoas com idade acima da média

 - exe095 = Aprimore o DESAFIO 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

---

**AULA 20 Funções/def (pt.1):**

Funções são rotinas, exemplo de algumas funções que já usamos e que já vem no python:
print(), len(), input(), int(), float() 
"def" são Funções você mesmo cria, ex:

	print('-' * 10)
	print('    SISTEMAS DE ALUNOS    ')
	print('-' * 10)
	print('-' * 10)
	print('    CADASTRO DE FUNCIONÁRIOS  ')
	print('-' * 10)
	print('-' * 10)
	print('    ERRO DO SISTEMA      ')
	print('-' * 10)

se eu criar:

	def mostralinha():
	   print('-' * 10)

e mandar printar assim:

	mostralinha()
	print('    SISTEMAS DE ALUNOS    ')
	mostralinha()
	mostralinha()
	print('    CADASTRO DE FUNCIONÁRIOS  ')
	mostralinha()
	mostralinha()
	print('    ERRO DO SISTEMA      ')
	mostralinha()

O print será o mesmo

Se eu usar as defs da seguinte maneira: 

 	def mensagem(msg):
	   print('-' * 15)
	   print(msg)
	   print('-' * 15)	
	mensagem('SISTEMAS DE ALUNOS')

quando o código rodar ele irá passar a mensagem 'SISTEMA DE ALUNOS' para o parâmetro msg

Caso queira somar dois números:
	
	def soma(a, b):
	    c = a + b
	    print(c)
	    
	# PROGRAMA PRINCIPAL
	n1 = int(input('N1: '))
	n2 = int(input('N2: '))
	soma(n1, n2)

Caso queira especificar qual será os números ou elementos da função faça assim

	def soma(a, b):
	    c = a + b
	    print(c)
	    
	# PROGRAMA PRINCIPAL
	soma(a=3, b=2) ou vice versa

mais exemplos:

	def soma(a, b):
	    print(f'A = {a} e B = {b}')
	    c = a + b
	    print(f'A soma A + B = {c}')
		    
	# PROGRAMA PRINCIPAL
	n1 = int(input('N1: '))
	n2 = int(input('N2: '))
	soma(a=n1, b=n2)
	soma(1, 3)

Caso queira que o def receba mais parâmetros do que o declarado basta colocar o def assim:

	"def soma(*num):"

Dessa maneira eu vou poder passar quantos parametros eu quiser, ex:

	def soma(*num):
	
	soma(2, 1, 7)
	soma(8, 0) 
	soma(4, 4, 7, 6, 0)

----------------------------------------------------------------
Códigos importantes:
 Def Para analisar a quantidade de valores recebidos:
	
 	def soma(* núm):
	   s = len(núm)
	   print(f'Recebi os valores {núm} e são ao todo {s} números')

	# Programa Principal
	soma(2, 1, 7)
	soma(8, 0) 
	soma(4, 4, 7, 6, 2)

-------
def que dobra valores:
	
 	def dob(lst):
	    s = 0
	    while s < len(lst):
	        lst[s] *= 2
	        s += 1
	
	# Programa Principal
	v = [3, 6, 5]
	dob(v) # O dobra vai receber os parâmetros do v
	print(v)

--------
def de Leitor e somador de números:

	def dob(* values):
	    s = 0
	    for n in values:
	        s += n
	    print(f'Somando os valores {values} temos {s}')
	
	# Programa Principal
	dob(int(input('Digite um valor: ')), 
	    int(input('Digite um valor: ')), 
	    int(input('Digite um valor: ')))

**Exercicios**

- exe096 = Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

- exe097 = Faça um programa que tenha a função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável. 

  -Ex:
  -  escreva('Olá, mundo!') 
  - Saida: ~~~~~~~~~~~~
            Olá, Mundo
           ~~~~~~~~~~~~

- exe098 = Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: inicio, fim e passo e realize a seguinte contagem.
-  Seu programa tem que realizar três contagens através da função criada:
-   a)De 1 até 10, de 1 em 1 
-   b)De 10 até 0, de 2 em 2
-   c)Uma contagem personalizada.

- exe099 = Faça um programa que tenha uma função que chamada maior(), que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior. 

- exe100 = Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores PARES sorteados pela função anterior. 

---

**AULA 21 Funções/Def (pt.2):**

 Nessa aula o professor falou sobre Interactive help, Parâmetros opcionais, Escopo de Variáveis, Retorno de Valores (return)

Interactive help:
	Para obter ajuda no python basta usar a função "help()" e colocar qual função está com duvida no terminal. Outra maneira de fazer isso basta usar o 	"print('funçâo'.__doc__)"

Docstring:	
	Para criar uma docstring para sua função basta 
	utilizar três aspas antes do inicio do código, Ex:

			def c(i, f, p):
   			 '''
    			=> Faz uma contagem e mostra na tela
   			:para i: inicio da contagem
    			:para f: fim da contagem
    			:para p: passo da contagem
    			:return: sem retorno    
    			 '''
    			c = i
    			while c <= f:
        			print(f'{c}', end='..')
        			c += p
    			print('FIM!')

			c(1, 10, 1)
			help(c)

Parâmetros Opcionais:

Os parâmetros Opcionais servem para verificar se há valores nas chamadas das defs, ex:

Definição de parâmetros opcionais:

Você define parâmetros opcionais dentro dos parênteses da função, atribuindo um valor padrão a eles. Por exemplo:

	def saudacao(nome, saudacao_padrao="Olá"):
	    mensagem = saudacao_padrao + ", " + nome
	    return mensagem

No exemplo acima, o parâmetro saudacao_padrao é opcional e tem um valor padrão de "Olá".

Chamada da função com parâmetros opcionais:

Quando você chama a função, pode fornecer argumentos apenas para os parâmetros obrigatórios ou pode incluir valores para os parâmetros opcionais, se desejar. Se você não fornecer um valor para um parâmetro opcional, o valor padrão será usado. 
ChatGPT

	def s(a=0, b=0, c=0):
    		s = a + b + c
    		print(f'A soma vale {s}')

	s(3, 2, 5)
	s(1,4)
	s()

Nesse código ele irá printar: 
A soma vale 10
A soma vale 5
A soma vale 0

O os 0 dentro da def s(a=0, b=0, c=0), servem para indicar se caso não estiver nenhum número dentro do chamado deles o indicie terá o valor 0.

Escopo de Variáveis:
Escopos de variáveis funcionam da seguinte maneira:

	==========================================
	|                                        |  
	| ==================================     |
	| | def escopo(b):                 |     |
	| |	                           |     |
	| |	a = 4                      |-----|------> ESCOPO LOCAL
	| |	b += 3                     |     |         a = [4]
	| |	c = 5                      |     |         b = [3]
	| |	print(f'A dentro vale {a}')|     |         c = [5]   
	| |	print(f'B dentro vale {b}')|     |
	| |	print(f'C dentro vale {c}')|     |
	| ==================================     |
	|                                        |
	| a = 5                                  |
	| b = 1                                  |
	| c = 4                                  |
	| escopo(a)                              |
	| print(f'A fora vale {a]')--------------|-------> ESCOPO GLOBAL
	| print(f'B fora vale {b}')              |	       a = [5]	 
	| print(f'C fora vale {c}')              |             b = [1]
	==========================================             c = [4]

Para tratar o A ou qualquer outra variável como global basta utilizar o "global a"

	==========================================
	|                                        |  
	| ==================================     |
	| | def escopo(b):                 |     |
	| |---> global a                   |     |
	| |	a = 4                      |-----|------> ESCOPO LOCAL
	| |	b += 3                     |     |         a = [4]<---------
	| |	c = 5                      |     |         b = [3]         |
	| |	print(f'A dentro vale {a}')|     |         c = [5]         |
	| |	print(f'B dentro vale {b}')|     |                         |
	| |	print(f'C dentro vale {c}')|     |                         |
	| ==================================     | Os "a" são iguais agora=|
	|                                        |                         |
	| a = 5                                  |                         |
	| b = 1                                  |                         |
	| c = 4                                  |                         | 
	| escopo(a)                              |                         |
	| print(f'A fora vale {a]')--------------|-------> ESCOPO GLOBAL   |
	| print(f'B fora vale {b}')              |	       a = [4]<----- 
	| print(f'C fora vale {c}')              |             b = [1]
	==========================================             c = [4]


Retorno de valores (return)

O "return" em Python é uma instrução usada em funções para especificar o valor que a função deve produzir como resultado quando é chamada. Aqui está uma explicação simples:                     ChatGPT

	def soma(n=1):
	    f = 1 
	    for c in range(n, 0, -1):
	        f *= c
	    return f

	a = int(input('Digite um numero para ver seu fatorial: '))
	print(f'O fatorial de {a} é igual a {soma(a)}')

**Exercicios**

- exe101 = Crie um programa que tenha uma função chamada voto que vai receber como parâmetro o ano de nascimento de uma pessoa. retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÒRIO nas eleições.

- exe102 = Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o nùmero a calcular e o outro chamado show, que será um valor lógico (opcional) indicando, se será mostrado ou não na tela o processo de cálculo do fatorial. 

- exe103 = Faça um programa que tenha uma função chamada ficha(), que os receba dois parâmetros opcionais: o nome dde um jogador e quantos gols ele marcou.
O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido formado corretamente

- exe104 = Crie um programa que tenha a função leiaint(), que vai funcionar de forma semelhante á função input() do python, só que fazendo validação para aceitar apenas um valor numérico.

		Ex:
		n = leiaint('Digite um n') 

- exe105 = Faça um programa que tenha uma função notas() que pode receber varias notas de alunos e vai retornar um dicionário com as seguintes informações:

   - Quantidade de notas 
   - A maior nota 
   - A menor nota
   - A média da turma
   - A situação (Opcional)
Adione também as docstrings da função.

- exe106 = Faça um mini-sistema que utilize o interactive help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará Obs: use cores.

---

**AULA 22 MÓDULOS E PACOTES**

Modularização 

- Surgiu no inicio da década de 60
- Sistemas ficando cada vez maiores
- Foco: Dividir um programa grande
- Foco: Aumentar a legibilidade
- Foco: facilitar a manutenção

Para explicar sobre a modularização o professor deu o seguinte exemplo:

	def fatorial(n):
	   f = 1
	   for c in range(1, n+1):
	      f *= c
	   return f
	
	num = int(input("Digite um valor: ")
	fat = fatorial(num)
	print(f'o fatorial de {num} é {fat}')

E logo após isso ele aumentou o tamanho do programa para dar o exemplo de como deve ser feito a modularização deixando-o assim: 
	
	# Defs
	def fact(n):
	    f = 1
	    for c in range(1, n+1):
	        f *= c
	    return f
	
	def dob(n):
	    return n * 2
	
	def tri(n):
	    return n * 3
	
	# Programa Principal
	num = int(input('Digite um valor: '))
	ff = fact(num) 
	print(f'O fatorial de {num} é {ff}')
	print(f'O dobro é {dob(num)}')
	print(f'E o triplo é {tri(num)}')

Após ter feito isso ele Passou as defs para um outro código e deixou apenas o programa principal no codigo e ficou assim 

	# Programa Principal
	num = int(input('Digite um valor: '))
	ff = fact(num) 
	print(f'O fatorial de {num} é {ff}')
	print(f'O dobro é {dob(num)}')
	print(f'E o triplo é {tri(num)}')

E após isso ele importou a função fact, dob, tri do outro código(Nosso caso u) e então ficou assim

	# Codigo principal da pagina app.py  
	  import u # <- Vai importar as defs da página u
	
	  num = int(input('Digite um valor: '))
	  ff = u.fact(num) 
	  print(f'O fatorial de {num} é {ff}')
	  print(f'O dobro é {u.dob(num)}')
	  print(f'E o triplo é {u.tri(num)}')
	
	# Codigo u importado para a o Codigo Principal 
	 def fact(n):
	    f = 1
	    for c in range(1, n+1):
	        f *= c
	    return f
	
	  def dob(n):
	     return n * 2
	
	  def tri(n):
	     return n * 3

ATENÇÃO!!!!!! NÃO ESQUECER DE SALVAR AS DEFS DA PÁGINA DE DEFS ANTES DE RODAR O PROGRAMA PRINCIPAL

Modulos que já vem no Python:

	from math import sqrt
	from datetime import date
	from random import randint

Vantagens da modularização:
- Organização do Código
- Facilita na manuntenção
- Ocultação do código detalhado
- Reutilização em outros projetos


  ⇧ E ESSE É O CONCEITO BÁSICO DE MODULARIZAÇÃO ⇧ 

Pacotes

Pacotes em python serve para reunir vários modulos, e para criar um é muito simples basta criar na pasta do projeto o nome do pacote que está armazenado os modulos, ex:

     Pasta =      Uteis
     Modúlos =     ↳ Cores 
	           ↳ Datas
	           ↳ Números   
	           ↳ Strings  
	

**Exercicios**

- exe107 = Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade() 
  - Faça também um programa que importe esse módulo e use algumas dessas funções

- exe108 = Adapte o código do desafio 107, criando uma função adicional chamada moeda() que consiga mostrar os valores como um valor monetário formatado

- exe109 = Modifique as funções que foram criadas no desafio 107 para que eles aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108

- exe110 = Adicione ao módulo moeda.py criado nos desafios anteriores, uma função chamada resummo(), que mostre ba tela algumas funções que já temos no módulo criado até aqui. 

- exe111 =  Crie um pacote chamado utilidadesCev que tenha dois módulos interno chamados moeda e dado.
  - Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando. 

- exe112 = Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado. crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função input(), mas com uma validação de dados para aceitar apenas valores que sejam monetários

---

**AULA 23 TRATAMENTO DE ERROS:**

Nesta aula o professor nos ensinou sobre os erros que normalmente acontecem no nosso código em Python, e ele deu o seguinte exemplo:

		print(x)

O código acima será uma exceção, mais conhecido como "NameError". Mais uma exceção a seguir:

		n = int(input('Num'))

Esse código irá rodar normalmente e dará um erro apenas se você digite algo que não seja um número inteiro, se o usuário digitar algo que não seja um número inteiro acontecerá um erro conhecido como "ValueError".

Mais um exemplo a seguir: 

		a = int(input('Numerador: '))
		b = int(input('Denominador: '))
		r = a / b
		print(f'O resultado é {r}')

O código rodará normalmente, porém se o usuário digitar 0, ele dará erro, por que não é possivel dividir 0, o nome desse erro em Python é "ZeroDivisionError"

Mais um exemplo: 

	r = 2 / '2'

O '2' è um número?, Em outras linguagens de programação como php e javascript ele seria, mas no Python não, logo ele dará um erro de tipo o "TypeError"

Exemplo de exceção utilizando listas:

	lst = [3, 6, 4]
	print(lst[3])

Esse código será uma exceção, pois o terceiro número da lista não existe. 

E se nós importarmos um módulo que não existe, o Erro que acontecerá será o "ModuleNotFoundError" ex:

import uteis

Caso uteis não exista esse código será uma exceção

No caso do Python toda exceção é filho de uma classe maior, Conhecida como "Exeption", e daí começamos a falar sobre o "try:" e o "except:' ex:

	try:
	 OPERAÇÃO
	
	except:
	 FALHOU

Ex utilizando os comandos: 

	try:    
	  a = int(input('Numerador: '))   
	  b = int(input('Denominador: '))
	  r = a / b
	  print(f'O resultado é {r}')
	
	except ZeroDivisionError():
	  print('\033[31mNão é possivel dividir 0\033[m')

E se o programa der certo podemos utilizar o "else:", para nos informar se deu certo ex: 

	try:    
	  a = int(input('Numerador: '))   
	  b = int(input('Denominador: '))
	  r = a / b
	
	except:
	  print('\033[31mTivemos um problema\033[m')
	
	else:
	  print(f'O resultado é {r}')

E por fim o professor nós explicou para que serve o "finally", tambem pode ser usado no código acima e ele acontecerá independente se o código deu erro ou não, Ex:

	try:    
	  a = int(input('Numerador: '))   
	  b = int(input('Denominador: '))
	  r = a / b
	
	except:
	  print('\033[31mTivemos um problema\033[m')
	
	else:
	  print(f'O resultado é {r:.1f}')
	
	finally:
	  print('Volte sempre!  Muito obrigado!!')

Ex utilizando o finally e o Exeption:

	try:    
	  a = int(input('Numerador: '))   
	  b = int(input('Denominador: '))
	  r = a / b
	
	except Exception as erro:
	  print(f'\033[31mTivemos um problema\033[m, O erro encontrado foi {erro.__class__}')
	
	else:
	  print(f'O resultado é {r:.1f}')
	
	finally:
	  print('Volte sempre! Muito obrigado!!')

Desta maneira podemos expandir nosso código de diversas maneiras explorando todos os tipos de exceção, ex:

	try:    
	  a = int(input('Numerador: '))   
	  b = int(input('Denominador: '))
	  r = a / b

	except (ValueError, TypeError):
   	  print(f'\033[31mTivemos um problema com os tipos de dados que você digitou.\033[m')

	except ZeroDivisionError:
	  print('\033[31mNão é possivel dividir um número por 0!\033[m')

	except KeyboardInterrupt:
	  print('\033[31mO usuário preferiu não informar os dados!\033[m')

	except Exception as erro:
    	  print(f'O erro encontrado foi {erro.__cause__}')
	
	else:
	  print(f'O resultado é {r:.1f}')

	finally:
	  print('Volte sempre! Muito obrigado!!')



**Exercicios**

- exe113  =  Reescreva a função leiaint() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função chamada leiaFloat() com a mesma funcionalidade.

- exe114  =  Crie um código em Python que teste se o site Pudim está acessivel pelo computador usado. 
 
- exe115 = Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples.
  
  - O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas. 
