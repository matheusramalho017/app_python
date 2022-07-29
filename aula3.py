
a = int(input('Insira a nota do primeiro bimestre: '))
while a > 10 or a < 0:
        a = int(input('Voce digitou errado! Insira novamente a nota do primeiro bimestre: '))
b = int(input('Insira a nota do Segundo bimestre: '))
while b > 10 or b < 0:
        b = int(input('Voce digitou errado! Insira novamente a nota do Segundo bimestre: '))
c = int(input('Insira a nota do terceiro bimestre: '))
while c > 10 or c < 0:
        c = int(input('Voce digitou errado! Insira novamente a nota do terceiro bimestre: '))
d = int(input('Insira a nota do quarto bimestre: '))
while d > 10 or d < 0:
        d = int(input('Voce digitou errado! Insira novamente a nota do quarto bimestre: '))

media = (a + b + c + d) / 4
print ('media: {}' .format(media))


# if a <= 10 and b <= 10 and c <= 10 and d <= 10:
#print ('media: {}' .format(media))
# else:
#     print('A nota informada de algum bimestre está errada')

#
# a = int(input('Entre com um valor: '))
# b = int(input('Entre com o segundo valor: '))
# resto_a = a%2
# resto_b = b%2
#
# if resto_a == 0 or not resto_b > 0:
#     print('TEM PAR')
# else:
#     print('NÃO TEM PAR BIXO')
#
# # a = int(input('Primeiro valor: '))
# # b = int(input('Segundo valor: '))
# # c = int(input('Terceiro valor: '))
# #
# # if a > b and a > c:
# #     print('O maior numero é: {}'.format(a))
# # elif b > a and b > c:
# #     print('O maior numero é: {}'.format(b))
# # else:
# #     print('O maior numero é: {}'.format(c))
# # print('Final do programa')