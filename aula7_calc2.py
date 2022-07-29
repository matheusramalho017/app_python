class Calculadora:

    def soma(self, valor_a, valor_b ):
        return valor_a + valor_b

    def sub(self, valor_a, valor_b ):
        return valor_a - valor_b

    def multi(self, valor_a, valor_b ):
        return valor_a * valor_b

    def divisao(self, valor_a, valor_b ):
        return valor_a / valor_b

if __name__ == '__main__':

    calculadora = Calculadora()
    print(calculadora.soma())
    print(calculadora.sub())
    print(calculadora.divisao())
    print(calculadora.multi())

