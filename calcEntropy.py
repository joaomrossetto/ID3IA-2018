from __future__ import division
import math as mt
import numpy as np
import copy as cp

def calculaEntropy(dados):
    positivo = getProporcaoPositiva(dados)
    negativo = getProporcaoNegativa(dados)
    positivo = round(positivo, 8)
    negativo = round(negativo, 8)
    entropia = ( -1*(positivo*mt.log(positivo,2)) - (negativo*mt.log(negativo,2)) )
    entropia = round(entropia, 8)
    return entropia

def getIndiceAtributo(dados, atributo):
    numColunas = len(dados[0])
    for indiceAtributo in range(0, numColunas):
        if dados[0][indiceAtributo] == atributo:
            #print(indiceAtributo)
            return indiceAtributo

def getProporcaoPositiva(dados):
    tam = len(dados[0])-1
    total = len(dados)
    positivos = 0
    for i in range (1, total):
        if dados[i][tam] == 'Yes':
            positivos += 1
    proporcao = round((positivos/(total-1)), 8)  #total-1 pq header entra na contagem do vetor
    return proporcao

def getProporcaoNegativa(dados):
    tam = len(dados[0])-1
    total = len(dados)
    negativos = 0
    for i in range (1, total):
        if dados[i][tam] == 'No':
            negativos += 1
    proporcao = round((negativos/(total-1)), 8) #total-1 pq header entra na contagem do vetor
    return proporcao

def makeConjuntoAtributo(dados,atributo,valorAtributo):
    indice= getIndiceAtributo(dados,atributo)
    tam = len(dados)
    j = 0
    novoconjunto = []
    for i in range(1, tam):
        if dados[i][indice] == valorAtributo:
            novoconjunto.append(dados[i])
    return novoconjunto

def getValoresAtributos(dados, atributo):
    indiceAtributo = getIndiceAtributo(dados, atributo)
    tam = len(dados)
    valores = []
    for i in range(1,tam):
        valores.append(dados[i][indiceAtributo])
    valores = set(valores)
    return sorted(valores)

def calculaGanhoInformacao(dados):
    entropiaGeral = calculaEntropy(dados)
    numAtributos = len(dados[0])
    numTotal = len(dados)-1
    valoresAtributo = []
    entropiasPorAtributo = []
    for i in range(1,numAtributos-1): #comeca em 1 considerando o atual dataset, ha uma coluna que nao se trata de atributo e eh apenas indice dos dias e a ultima eh o rotulo
        entropiasPorAtributo.append(dados[0][i])
        print(entropiasPorAtributo)
        valoresAtributo.append(getValoresAtributos(dados, dados[0][i]))
        print(valoresAtributo)
    for x in range(0, len(valoresAtributo)): #sepa é valoresAtributo -1
        entropiaTemporario = []
        for j in range(0,len(valoresAtributo[x])):
            entropiaTemporario.append(calculaEntropy(makeConjuntoAtributo(dados,dados[0][x],valoresAtributo[x][j])))  #armazenando entropia do conjunto de cada atributo


