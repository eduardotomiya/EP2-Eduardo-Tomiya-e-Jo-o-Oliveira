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
