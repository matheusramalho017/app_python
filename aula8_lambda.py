contador_letras = lambda lista: [len(x) for x in lista]

lista_animais = ['cachorro', 'gato', 'elefante']
print(contador_letras(lista_animais))

soma = lambda a, b: a+b
sub = lambda a,b: a-b

print(soma(5, 10))
print(sub(1, 5))

calculadora = {
    'soma': lambda a, b: a+b,
    'subtração':  lambda a,b: a-b,
    'divisão':   lambda a,b: a/b,
    'multiplicação':   lambda a,b: a*b,
    'resto':   lambda a,b: a%b
}

print (type(calculadora))
soma = calculadora['soma']
sub =  calculadora['subtração']
print('A soma é: {}'.format(soma(10, 5)))
print('A subtração é: {}'.format(sub(5, 5)))