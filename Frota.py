def afundados(frota, tabuleiro):
    soma = 0
    for navio in frota:
        afundado = True
        for coordenada in navio["posicoes"]:
            if tabuleiro[coordenada[0]][coordenada[1]] != "X":
                afundado = False
                break
        if afundado:
            soma += 1
    return soma


def define_posicoes(linha, coluna, orientacao, tamanho):
        posicao = []
        posicao.append([linha, coluna])
        i = 0
        if orientacao == "vertical":
            while i < tamanho - 1:
                linha += 1
                i += 1
                posicao.append([linha, coluna])
        elif orientacao == "horizontal":
            while i < tamanho - 1:
                coluna += 1
                i += 1
                posicao.append([linha, coluna])
        return posicao



def faz_jogada(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = "X"
    else:
        tabuleiro[linha][coluna] = "-"

    return tabuleiro