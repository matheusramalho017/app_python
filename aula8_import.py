from aula7_TV import Televisao
from aula7_calc1 import Calculadora
from aula8_contador_letras import contador_letras, teste

if __name__ == '__main__':

    televisao = Televisao()
    print(televisao.ligada)
    televisao.power()
    print(televisao.ligada)
    calculadora = Calculadora(10, 4)
    print(calculadora.soma())
    lista = ['cachorro', 'gato', 'elefante']
    total_letras = contador_letras(lista)
    print('o total de letras por palavra da lista: {}'.format(total_letras))
    print(teste())