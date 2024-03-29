import random

# PARA TESTAS O SEU CÓDIGO NA ACADEMIA PYTHON SERÁ NECESSÁRIO COLAR AS FUNÇÕES DESENVOLVIDAS AQUI!!!

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

def posiciona_frota(frota):
    matriz = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    for navio in frota:
        tipo = navio["tipo"]
        posicoes = navio["posicoes"]

        for posicao in posicoes:
            linha, coluna = posicao
            matriz[linha][coluna] = 1

    return matriz




def preenche_frota(dados_posicionamento, nome_navio, frota):
    linha = dados_posicionamento['linha']
    coluna = dados_posicionamento['coluna']
    orientacao = dados_posicionamento['orientacao']
    tamanho = dados_posicionamento['tamanho']

    novas_posicoes = define_posicoes(linha, coluna, orientacao, tamanho)
    novo_navio = {
        'tipo': nome_navio,
        'posicoes': novas_posicoes
    }

    frota.append(novo_navio)
    return frota






def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
    '''
    tabuleiro_jogador: tabuleiro do jogador
    tabuleiro_oponente: tabuleiro do oponente
    Função monta uma string com a representação dos tabuleiros do jogador e do oponente.
    O tabuleiro do jogador é representado por um tabuleiro com as posições dos navios.
    O tabuleiro do oponente é representado por um tabuleiro com as posições que o jogador já atirou.
    '''

    texto = ''
    texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
    texto += '_______________________________      _______________________________\n'

    for linha in range(len(tabuleiro_jogador)):
        jogador_info = '  '.join([str(item)
                                  for item in tabuleiro_jogador[linha]])
        oponente_info = '  '.join(
            [info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
        texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
    texto += '_______________________________      _______________________________\n'
    return texto


def gerando_frota_automaticamente():
    '''
    Função gera uma frota de navios de forma aleatória.
    '''
    quantidades = {
        "submarino": {
            "quantidade": 4,
            "tamanho": 1
        },
        "destroyer": {
            "quantidade": 3,
            "tamanho": 2
        },
        "navio-tanque": {
            "quantidade": 2,
            "tamanho": 3
        },
        "porta-aviões": {
            "quantidade": 1,
            "tamanho": 4
        }
    }

    frota = []

    for nome_navio, info in quantidades.items():
        for _ in range(info["quantidade"]):
            dados_de_posicionamento = {
                "tamanho": info["tamanho"],
            }
            dados_de_posicionamento["orientacao"] = random.choice(
                ["vertical", "horizontal"])
            dados_de_posicionamento["linha"] = random.randint(0, 9)
            dados_de_posicionamento["coluna"] = random.randint(0, 9)

            while not posicao_valida(dados_de_posicionamento, frota):
                dados_de_posicionamento["orientacao"] = random.choice(
                    ["vertical", "horizontal"])
                dados_de_posicionamento["linha"] = random.randint(0, 9)
                dados_de_posicionamento["coluna"] = random.randint(0, 9)

            preenche_frota(dados_de_posicionamento, nome_navio, frota)

    return frota


# Gerando frota de forma aleatório para jogadores
frota_jogador = gerando_frota_automaticamente()
frota_oponente = gerando_frota_automaticamente()

# Criando tabuleiro com as frotas posicionadas
tabuleiro_jogador = posiciona_frota(frota_jogador)
tabuleiro_oponente = posiciona_frota(frota_oponente)
jogando = True
while jogando:

    # Imprimindo tabuleiro
    print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))

    # TODO: Implemente aqui a lógica para perguntar a linha que o jogador deseja atirar
    # TODO: Implemente aqui a lógica para perguntar a coluna que o jogador deseja atirar
    # TODO: Implemente aqui a lógica para verificar se a linha e coluna não foram escolhidas anteriormente
    # TODO: Implemente aqui a lógica para verificar se o jogador derrubou todos os navios do oponente
