from time import sleep


def leiatxt(arq):
    arquivo = open(f'./utilidadescev/_arquivos/{arq}', mode='r', encoding='UTF-8')

    for linha in arquivo:
        print(linha)
    arquivo.close()


def escreva(palavra):
    # Abra o arquivo (leitura)
    arquivo = open(f'./utilidadescev/_arquivos/dados.txt', mode='r', encoding='UTF-8')
    conteudo = arquivo.readlines()

    # insira seu conteúdo
    # obs: o método append() é proveniente de uma lista
    conteudo.append(palavra)

    # Abre novamente o arquivo (escrita)
    # e escreva o conteúdo criado anteriormente nele.
    arquivo = open(f'./utilidadescev/_arquivos/dados.txt', mode='w', encoding='UTF-8')
    arquivo.writelines(conteudo)
    arquivo.writelines('\n')
    arquivo.close()


def cadastro(nome, idade):
    arquivo = open(f'./utilidadescev/_arquivos/dados.txt', mode='r', encoding='UTF-8')
    conteudo = arquivo.readlines()
    conteudo.append(nome + '\t' * 8 + str(idade))
    arquivo = open(f'./utilidadescev/_arquivos/dados.txt', mode='w', encoding='UTF-8')
    arquivo.writelines(conteudo)
    arquivo.writelines('\n')
    arquivo.close()
    sleep(0.5)
    print('Cadastrado com Sucesso!')
    sleep(0.5)
