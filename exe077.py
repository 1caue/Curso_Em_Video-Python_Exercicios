tup = ('Aprender', 'Programar',
       'Linguagem', 'Python',
       'Curso', 'Grátis', 'Estudar'
       'Praticar', 'Trabalhar', 'Mercado'
       'Programador', 'Futuro')
for i in tup:
    print(f'\nNa palavra {i} temos ', end='') 
    for let in i:
        if let.lower() in 'aeiou':
            print(let, end=' ')
