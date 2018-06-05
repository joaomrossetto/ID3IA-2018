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
    for i in range (0, total):
        if dados[i][tam] == 'Yes':
            positivos += 1
    proporcao = round((positivos/(total-1)), 8)  #total-1 pq header entra na contagem do vetor
    return proporcao

def getProporcaoNegativa(dados):
    tam = len(dados[0])-1
    total = len(dados)
    negativos = 0
    for i in range (0, total):
        if dados[i][tam] == 'No':
            negativos += 1
    proporcao = round((negativos/(total-1)), 8) #total-1 pq header entra na contagem do vetor
    return proporcao

def getNumeroAparicoes(dados, atributo, valorAtributo):
    indice = getIndiceAtributo(dados,atributo)
    contador = 0
    for i in range (0, len(dados)):
        if dados[i][indice] == valorAtributo:
            contador += 1
    return contador

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

def calculaEntropiaTemporario(dados):
    return (-1)*dados[2]*dados[1]

def calculaGanhoInformacao(dados, atributo):
    entropiaGeral = calculaEntropy(dados)
    numTotal = len(dados)-1
    valoresAtributo = getValoresAtributos(dados, atributo)
    entropiaTemporario = [[0 for x in range(0,3)] for y in range(0,len(valoresAtributo))]
    for x in range(0, len(valoresAtributo)):
        entropiaTemporario[x][0] = valoresAtributo[x]
        entropiaTemporario[x][1] = calculaEntropy(makeConjuntoAtributo(dados, atributo, valoresAtributo[x]))
        entropiaTemporario[x][2] = (getNumeroAparicoes(dados,atributo,valoresAtributo[x])/numTotal)
    print(entropiaTemporario)
    ganhodeinfo=0
    for n in range(0,len(valoresAtributo)):
        ganhodeinfo = ganhodeinfo + calculaEntropiaTemporario(entropiaTemporario[n])

    print(ganhodeinfo)




