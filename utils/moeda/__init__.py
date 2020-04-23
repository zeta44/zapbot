def aumentar(preço=0, taxa=0, formato=False):
    res = preço + (preço * taxa/100)
    return res if format is False else moeda(res)


def diminuir(preço=0, taxa=0, formato=False):
    res = preço - (preço * taxa / 100)
    return res if format is False else moeda(res)


def dobro(preço=0, formato=False):
    res = preço * 2
    return res if format is False else moeda(res)


def metade(preço=0, formato=False):
    res = preço / 2
    return res if format is False else moeda(res)


def moeda(preço=0, moeda='R$ '):
    return f'{moeda}{preço:>.2f}'.replace('.', ',')


def resumo(preço=0, taxaa=0, taxar=0):
    tab = '\t'
    if taxar < 10:
        tab = '\t\t'
    else:
        tab = '\t'
    fator = 30
    lin = '-' * fator
    print(lin)
    print('RESUMO DO VALOR'.center(fator))
    print(lin)
    print(f'Preço analisaso: \t{moeda(preço)}')
    print(f'O dobro do preço: \t{dobro(preço, True)}')
    print(f'Mwtade do preço: \t{metade(preço, True)}')
    print(f'{taxaa}% de aumento: \t{aumentar(preço, taxaa, True)}')
    print(f'{taxar}% de redução: {tab}{diminuir(preço, taxar, True)}')
    print(lin)
