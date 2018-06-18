'''Faz a acuracia com o nó, sem o nó e compara. Se a acuracia for maior sem ele, remove. O nó somente é removido se a árvore removida
não for pior que a original no conjunto de validação.'''

def poda1 (Root, Exemplos)
    acuraciaAntiga = classificador(Exemplos,Root)
    novoNo = deepcopy(Root)

    if len(novoNo.filhos) != 0:
        novoNo.filhos = {}
        acuraciaNova = classificador(Exemplos,novoNo)
        if acuraciaNova > acuraciaAntiga:
            Root.filhos = {}
            return Root
    return Root

def poda2 (Root, Exemplos)
    temp = []
    saida = []
    temp.append(Root)
    while len(temp) != 0:
        n = temp.pop(0)
        n = poda1(n, Exemplos)
        filhos = n.filhos
        if len(filhos) != 0:
            for i in filhos.itervalues():
                temp.append(i)
    return Root
