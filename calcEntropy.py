import math as mt
import numpy as np

def calculaEntropy(dados):
    positivo = getProporcaoPositiva(dados)
    negativo = getProporcaoNegativa(dados)
    positivo = round(positivo, 8)
    negativo = round(negativo, 8)
    entropia = ( -(positivo*mt.log(positivo,2)) - (negativo*mt.log(negativo,2)) )
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
    proporcao = round(positivos/(total-1), 8) #total-1 pq header entra na contagem do vetor
    return proporcao

def getProporcaoNegativa(dados):
    tam = len(dados[0])-1
    total = len(dados)
    negativos = 0
    for i in range (1, total):
        if dados[i][tam] == 'No':
            negativos += 1
    proporcao = round(negativos/(total-1), 8) #total-1 pq header entra na contagem do vetor
    return proporcao

def makeConjuntoAtributo(dados,atributo):



def getValoresAtributos(dados, atributo):
    indiceAtributo = getIndiceAtributo(dados, atributo)
    tam = len(dados)
    valores = []
    for i in range(1,tam):
        valores.append(dados[i][indiceAtributo])
    valores = set(valores)
    return sorted(valores)

def calculaGanhoInformacao(dados, atributo):
    entropiaGeral = calculaEntropy(dados)

