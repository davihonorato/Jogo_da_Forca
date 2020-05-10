from game.lib import *

inicio()
dica = dica()
palavra = palavraChave(dica)
palavra_oculta = palavraOculta(palavra)

erros = 0
while erros != 6 and palavra_oculta != palavra:
    menu(palavra_oculta, erros, dica)
    player = letra('\nDigite uma letra: ')
    palavra_oculta = atualizar(player, palavra, palavra_oculta)
    if not verificar(player, palavra_oculta):
        erros += 1
resultado(palavra, palavra_oculta, erros)
