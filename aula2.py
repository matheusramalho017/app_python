a = int(input('Entre com o primeiro numero: '))
b = int(input('Entre com o segundo numero: '))
soma = a+b
sub = a-b
multi = a*b
divi = a/b
resto = a%b
resultado = ('Soma: {soma}. \nSubtração: {sub}. '
      '\nMultiplicação: {multi}. '
      '\nDivisão: {divi}. '
      '\nResto: {resto}'.format(soma=soma,
                            sub=sub,
                            multi=multi,
                            divi=divi,
                            resto=resto))
print(resultado)
#print('Soma: {}. Subtração: {}'.format(soma, sub))
#x = '1'
#soma2 = int(x)
#print (soma2)