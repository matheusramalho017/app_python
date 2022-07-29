class Error(Exception):
        pass

class InputError(Error):
    def __init__(self, message):
        self.message = message

while True:
    try:
        x = int(input('Entre com uma nota de 0 a 10: '))
        print(x)
        if x > 10:
            raise InputError('\nNota não pode ser maior que 10\n')
        elif x < 0:
            raise InputError('\nNota não pode ser menor que 0\n')
        break
    except ValueError:
        print('\nValor inválido!\n')
    except InputError as ex:
        print(ex)