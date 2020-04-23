def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31mERRO:\"{entrada}\" é um preço inválido!\033[m')
        else:
            valido = True
            return float(entrada)


def leiaInt(msg):
    while True:
        try:
            num = int(input(msg).strip())

        except (ValueError, TypeError):
            print('\033[0;31mNão é um número inteiro.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[0;31mO usuário prefiriu não digitar\033{m')
            return 0
        else:
            return num


def leiaFloat(msg):
    while True:
        try:
            num = float(input(msg).replace(',', '.').strip())
        except (ValueError, TypeError):
            print('\033[0;31mNão é um número real.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[0;31mO usuário prefiriu não digitar\033{m')
            return 0
        else:
            return num


def leiaStr(msg):
    while True:
        try:
            obj = str(input(msg).title().strip())
        except (ValueError, TypeError):
            print('\033[0;31mNão é uma palavra.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[0;31mO usuário prefiriu não digitar\033{m')
            return 0
        else:
            return obj
