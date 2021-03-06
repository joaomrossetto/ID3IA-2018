from __future__ import division
import calcEntropyPlayTennis as calc
from Node import Node
from copy import deepcopy

def ValorMaisComum(Dados, Target, Atributos):
    MaisComum = ''
    ganhaMais = calc.getNumeroAparicoes(Dados, Target, "Yes")
    ganhaMenos = calc.getNumeroAparicoes(Dados, Target, "No")
    if ganhaMais > ganhaMenos:
        MaisComum = 'Yes'
    else:
        MaisComum = 'No'
    return MaisComum


def MelhorAtributo(Dados, Atributos):
    Melhor = Atributos[0]
    Ganho = 0
    numAtributos = len(Atributos) - 1
    for i in range(0, numAtributos):
        if i == 0:
            Ganho = calc.calculaGanhoInformacao(Dados, Atributos[i])
        NovoGanho = calc.calculaGanhoInformacao(Dados, Atributos[i])
        # print(Atributos[i])
        # print(NovoGanho)
        if NovoGanho > Ganho:
            Ganho = NovoGanho
            Melhor = Atributos[i]
    return Melhor


def Excluir_vetor(vetor, atributo):
    tam = len(vetor)
    novoconjunto = []
    for i in range(0, tam):
        if vetor[i] != atributo:
            novoconjunto.append(vetor[i])
    return novoconjunto


def ArvoreDecisao(Dados, Target, Atributos, default):
    Root = Node()

    indice = calc.getIndiceAtributo(Dados, Target)
    maior = "No"
    menor = "Yes"
    imaior = 0
    imenor = 0
    a = ""
    for i in range(1, len(Dados)):
        if imaior > 0 and imenor > 0:
            break
        elif Dados[i][indice] == maior:
            imaior = imaior + 1
        elif Dados[i][indice] == menor:
            imenor = imenor + 1
    #### se tudo for igual
    if imenor == len(Dados) - 1:
        # return Tree.novo_no(menor)
        return menor
    elif imaior == len(Dados) - 1:
        # return Tree.novo_no(maior)
        return maior

    ##se acabarem os atributos
    if len(Atributos) == 1:
        return ValorMaisComum(Dados, Target, Atributos)
    # return Tree.novo_no(ValorMaisComum(Dados,Target,Atributos))
    else:
        a = MelhorAtributo(Dados, Atributos)
        Root.atributo = a
        filhos = {}
        # print("Atributo: " + a)
        Valores_A = calc.getValoresAtributos(Dados, a)
        # for ind in range(0,len(Atributos)):
        #   if Atributos[ind]==a:
        #       break

        for y in range(0, len(Valores_A)):
            Subconjunto = []
            Subconjunto = calc.makeConjuntoAtributo(Dados, a, Valores_A[y])
            # print("Valor: " +Valores_A[y])
            if len(Subconjunto) == 1:
                # print(ValorMaisComum(Dados,Target,Atributos))
                return Root
            else:
                filhos[Valores_A[y]] = ArvoreDecisao(Subconjunto, Target, Excluir_vetor(Atributos, a), Root)
                Root.filhos = filhos

    return Root


def classificador(Dados, Arvore):
    numeroExemplos = len(Dados)
    numAcertos = 0
    acuracia = 0
    indiceClasse = calc.getIndiceAtributo(Dados, 'play')
    for i in range(1, len(Dados)):
        classeExemplo = Dados[i][indiceClasse]
        classeReal = avaliaExemplo(Arvore, Dados[i], Dados)
        if classeExemplo == classeReal:
            numAcertos += 1
        acuracia = numAcertos / (numeroExemplos - 1)
    print("A acuracia foi de :", acuracia)
    return acuracia


def avaliaExemplo(NoRaiz, Exemplo, Dados):
    nosVisitados = 0
    while len(NoRaiz.filhos) != 0:
        atributoNo = NoRaiz.atributo
        indiceAtributo = calc.getIndiceAtributo(Dados, atributoNo)
        valorAtributoExemplo = Exemplo[indiceAtributo]
        valorAtributoAux =""
        for a in NoRaiz.filhos:
           if valorAtributoAux == "":
              valorAtributoAux = a 
           elif valorAtributoExemplo == a:
                valorAtributoAux = a
        NoRaiz = NoRaiz.filhos[valorAtributoAux]
        nosVisitados += 1
        if NoRaiz == 'No' or NoRaiz == 'Yes':
            return NoRaiz
    return NoRaiz

def poda1 (Root, Dados):
    acuraciaAntiga = classificador(Dados,Root)
    novoNo = deepcopy(Root)
    if len(novoNo.filhos) != 0:
        novoNo.filhos = {}
        acuraciaNova = classificador(Dados,novoNo)
        if acuraciaNova > acuraciaAntiga:
            Root.filhos = {}
            return Root
    return Root

def poda2 (Root, Dados):
    temp = []
    temp.append(Root)
    while len(temp) != 0:
        n = temp.pop(0)
        n = poda1(n, Dados)
        filhos = n.filhos
        if len(filhos) != 0:
            for i in filhos:
                if filhos[i] != 'No' and filhos[i] != 'Yes':
                     temp.append(filhos[i])
    return Root












