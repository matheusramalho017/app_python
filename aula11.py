
lista = [1, 10]
arquivo = open('teste.txt', 'r')
try:
    divisao = 10 / 2
    numero = lista[1]

except ZeroDivisionError:
    print('Não é possível dividir por 0')
except ArithmeticError:
    print('Erro aritmético')
except IndexError:
    print('Erro desconhecido (indice invalido na lista)')
except Exception as ex:
    print('erro desconhecido. Erro{}'.format(ex))
else:
    print('Executa quando não ocorre nenhuma exceção')
finally:
    print('Sempre executa')
    print('Fechando arquivo')
    arquivo.close()
