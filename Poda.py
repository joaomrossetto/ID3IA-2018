#Faz a acuracia com o nó, sem o nó e compara. Se a acuracia for maior sem ele, remove 

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

''''Takes in a trained tree and a validation set of examples.  Prunes nodes in order
  to improve accuracy on the validation data; the precise pruning strategy is up to you.
  *pruning strategy - removing subtree rooted at node, making it a leaf node with the most common classification of the training examples affiliated with that node
                    - node removed only if pruned tree performs no worse than the original over the validation set
                    - pruning continues until further pruning is harmful (reduced error pruning algorithm)'''

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
