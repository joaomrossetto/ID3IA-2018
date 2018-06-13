from __future__ import division
import pandas as pd
import numpy as np
import calcEntropy as calc
import arvoreDecisao as decisao
import Tree

jogaTenis = pd.read_csv('playtennis.csv', sep=',', header = None)
jogaTenis = jogaTenis.values
print(jogaTenis)
indiceDoAtributo = calc.getIndiceAtributo(jogaTenis, 'temp')
print(indiceDoAtributo)
arvore = Tree.Arvore()
decisao.ArvoreDecisao(jogaTenis,'play',jogaTenis[0],arvore)
arvore.display("outlook")
#print(calc.makeConjuntoAtributo(jogaTenis,"outlook","Overcast"))
#print(calc.getProporcaoPositiva(calc.makeConjuntoAtributo(jogaTenis,"outlook","Rain")))
#print(calc.getProporcaoNegativa(calc.makeConjuntoAtributo(jogaTenis,"outlook","Rain")))
#valoresAtributo = calc.getValoresAtributos(jogaTenis,"temp")
#print(valoresAtributo[0])
#calc.calculaGanhoInformacao(jogaTenis,"outlook")
#calc.calculaGanhoInformacao(jogaTenis,"temp")
#calc.calculaGanhoInformacao(jogaTenis,"humidity")
#calc.calculaGanhoInformacao(jogaTenis,"wind")

