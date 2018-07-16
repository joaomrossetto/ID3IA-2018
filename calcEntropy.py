from __future__ import division
import math as mt
import numpy as np
import copy as cp

colunas = ['age','workclass','education','education.num','marital.status','occupation','relationship',
'race','sex','capital.gain','capital.loss','hours.per.week','native.country','X50k.year']

def calculaEntropy(dados):
    positivo = getProporcaoPositiva(dados)
    negativo = 1 - positivo
    positivo = round(positivo, 4)
    negativo = round(negativo, 4)
    if positivo == 0:
        logAuxPos = 0
    else:
        logAuxPos = positivo * mt.log(positivo, 2)
    if negativo == 0:
        logAuxNeg = 0
    else:
        logAuxNeg = negativo * mt.log(negativo, 2)
    entropia = ( -(logAuxPos) - (logAuxNeg))
    entropia = round(entropia,6)
    return entropia

def getIndiceAtributo(atributo):
    numColunas = len(colunas)
    for indiceAtributo in range(0, numColunas):
        if colunas[indiceAtributo] == atributo:
            #print(indiceAtributo)
            return indiceAtributo

def getProporcaoPositiva(dados):
    tam = len(dados[0])-1
    total = len(dados)
    positivos = 0
    for i in range (0, total):
        if dados[i][tam] == '<=50K':
            positivos += 1
    proporcao = positivos/(total-1)  #total-1 pq header entra na contagem do vetor
    proporcao = round(proporcao,6)
    return proporcao

def getProporcaoNegativa(dados):
    tam = len(dados[0])-1
    total = len(dados)
    negativos = 0
    for i in range (0, total):
        if dados[i][tam] == '>50K':
            negativos += 1
    proporcao = negativos/(total-1) #total-1 pq header entra na contagem do vetor
    proporcao = round(proporcao,6)
    return proporcao

def getNumeroAparicoes(dados, atributo, valorAtributo):
    indice = getIndiceAtributo(atributo)
    contador = 0
    for i in range (0, len(dados)):
        if dados[i][indice] == valorAtributo:
            contador += 1
    contador = round(contador,6)
    return contador

def makeConjuntoAtributo(dados,atributo,valorAtributo):
    indice= getIndiceAtributo(atributo)
    tam = len(dados)
    novoconjunto = []
    novoconjunto.append(colunas)
    for i in range(0, tam):
        if dados[i][indice] == valorAtributo:
            novoconjunto.append(dados[i])
    return novoconjunto

def getValoresAtributos(dados, atributo):
    indiceAtributo = getIndiceAtributo(atributo)
    tam = len(dados)
    valores = []
    for i in range(0,tam):
        valores.append(dados[i][indiceAtributo])
    valores = set(valores)
    return sorted(valores)

def calculaEntropiaTemporario(dados):
    aux = (-1)*dados[2]*dados[1]
    aux = round(aux,6)
    return aux

def calculaGanhoInformacao(dados, atributo):
    entropiaGeral = calculaEntropy(dados)
    numTotal = len(dados)-1
    valoresAtributo = getValoresAtributos(dados, atributo)
    entropiaTemporario = [[0 for x in range(0,3)] for y in range(0,len(valoresAtributo))]
    for x in range(0, len(valoresAtributo)):
        #print(makeConjuntoAtributo(dados, atributo, valoresAtributo[x]))
        entropiaTemporario[x][0] = valoresAtributo[x]
        entropiaTemporario[x][1] = round(calculaEntropy(makeConjuntoAtributo(dados, atributo, valoresAtributo[x])),6)
        entropiaTemporario[x][2] = round(getNumeroAparicoes(dados,atributo,valoresAtributo[x])/numTotal, 6)
    #print(entropiaTemporario)
    ganhodeinfo=0
    for n in range(0,len(valoresAtributo)):
        ganhodeinfo = ganhodeinfo + calculaEntropiaTemporario(entropiaTemporario[n])
    #print(ganhodeinfo)
    entropiaFinal = round(ganhodeinfo,6) + round(entropiaGeral,6)
    #print(entropiaFinal)
    return entropiaFinal