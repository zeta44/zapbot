def leiaInt(msg):
    while True:
        try:
            num = int(input(msg).strip())

        except (ValueError, TypeError):
            print('It is not an integer..')
            continue
        except KeyboardInterrupt:
            print('The user chose not to type.')
            return 0
        else:
            return num


def leiaFloat(msg):
    while True:
        try:
            num = float(input(msg).replace(',', '.').strip())
        except (ValueError, TypeError):
            print('Não é um número real.')
            continue
        except KeyboardInterrupt:
            print('The user chose not to type.')
            return 0
        else:
            return num


def leiaStr(msg):
    while True:
        try:
            obj = str(input(msg).title().strip())
        except (ValueError, TypeError):
            print('This is not a string.')
            continue
        except KeyboardInterrupt:
            print('The user chose not to type.')
            return 0
        else:
            return obj
