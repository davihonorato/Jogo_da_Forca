from random import choice, randint


def inicio():
    print('-' * 30)
    print(f'{"JOGO DA FORCA":-^30}')


def dica():  # Escolhe qual vai ser o tema da palavra
    lista = ['objetos.txt', 'frutas.txt']
    s = randint(0, 1)
    return lista[s]


def menu(oculta, erros, dica):  # Printa a "interface" do jogo.
    print('-' * 30)
    print(f'Erros: {erros}')
    print(f'Dica: {dica.replace(".txt", "")}')
    print('PALAVRA:', end=' ')
    for l in oculta:
        print(f'{l}', end=' ')


def palavraChave(chave):  # Escolhe a palavra com base na chave/dica (nome do arquivo) escolhida.
    try:
        with open(chave, 'rt') as r:
            p = r.readlines()
        palavra_escolhida = choice(p)
        palavra = palavra_escolhida.upper()
    except:
        print('Ocorreu um erro.')
    else:
        return list(palavra.replace('\n', ''))


def palavraOculta(palavra):  # Cria uma estrutura que exemplifique a palavra (famosos tracinhos/ espaços da letra).
    tam = len(palavra)
    lista = list()
    for c in range(0, tam):
        lista.append('_')
    return lista


def letra(txt):  # Identifica se a entrada é uma letra (e apenas uma; funciona como um input).
    letra = str(input(txt)).upper().strip()
    if not letra.isalpha():
        print('Digite uma letra válida.')
    else:
        return letra


def atualizar(usuario, palavra, oculta):  # Verifica se a letra do usuário está na palavra escolhida
    # e atualiza a palavra oculta.
    try:
        for c, j in enumerate(palavra):
            if usuario == j:
                oculta[c] = usuario
    except:
        print('Ocorreu um erro.')
    else:
        return oculta


def verificar(letra, oculta):  # Verifica se a letra adicionada pelo usuário se encontra
    # na palavra oculta (ocorre depois da palavra ser atualizada)
    if letra in oculta:
        return True


def resultado(palavra, oculta, erros):  # Printa o resultado final do usuário
    print('-' * 30)
    if oculta == palavra:
        print(f'Parabéns! A palavra era {"".join(palavra)}.')
        print(f'Total de erros: {erros}')
    else:
        print(f'Você perdeu! A palavra era {"".join(palavra)}. \nErros: {erros}')
