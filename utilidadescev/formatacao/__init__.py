from time import sleep


def cabecario(titulo):
    global lin
    lin = '-' * 40
    print(lin)
    print(f'{titulo:^40}')
    print(lin)
    sleep(0.5)


def rodape():
    print(lin)
    sleep(0.5)
